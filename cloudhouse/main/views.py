from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from rest_framework.generics import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password

from .models import *
from django.db.models import Q
from .serializers import ReportSensorsParamsSerializer, DevicesSerializer, VoiceSensorsSerializer, \
    EnergySensorsSerializer, ClientsSerializer, ContractsSerializer, UserSettingsSerializer, NotificationsSerializer, \
    TemperatureSensorsSerializer, LightSensorsSerializer, AddressesSerializer
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from .utils import body

date_notif = datetime.now()
datee = date_notif.date()
timee = date_notif.time()
one_month_later = datee + timedelta(days=30)


@login_required
def cabinet(request):
    if request.user.is_staff:
        return redirect('admin_panel')
    else:
        return render(request, 'main/account.html')


@login_required
def admin_panel(request):
    username = request.user.username
    user = User.objects.all()
    contract = Contracts.objects.filter(archive=0)
    client_ids = contract.values_list('client_id', flat=True)
    clientt = Clients.objects.filter(client_id__in=client_ids)
    user_ids = clientt.values_list('user_id', flat=True)
    settings = UserSettings.objects.filter(user_id__in=user_ids)
    notification = Notifications.objects.filter(user_id__in=user_ids)
    client = Clients.objects.filter(client_id__in=client_ids)
    archive = Contracts.objects.filter(archive=1)
    device = Devices.objects.filter(contract_code__archive=0)
    light = LightSensors.objects.filter(device__contract_code__archive=0)
    temp = TemperatureSensors.objects.filter(device__contract_code__archive=0)
    energy = EnergySensors.objects.filter(device__contract_code__archive=0)
    voice = VoiceSensors.objects.filter(device__contract_code__archive=0)
    report = ReportSensorsParams.objects.filter(user_id__in=user_ids)
    address = Addresses.objects.filter(code_contract__archive=0)
    context = {'user': user, 'username': username, 'contract': contract, 'settings': settings,
               'notification': notification, 'client': client,
               'report': report,
               'address': address, 'light': light, 'temp': temp, 'energy': energy, 'voice': voice,
               'device': device, 'data': datee, 'archives': archive}
    return render(request, 'main/adminpanel.html', context)


def ajaxbd(request):
    user = User.objects.get(id=request.user.id)
    client = user.clients
    cl = Clients.objects.get(user_id=user)
    settings = UserSettings.objects.get(user_id=user)
    notifications = Notifications.objects.filter(user_id=user).order_by('-notification_id')
    reports = ReportSensorsParams.objects.filter(user_id=user)
    count = Contracts.objects.filter(client=client, archive=0)
    contract_count = count.count()
    if contract_count == 1:
        contract_bd = Contracts.objects.get(client=client, archive=0)
        address_bd = Addresses.objects.get(code_contract=contract_bd.code_contract)
        device_bd = Devices.objects.get(contract_code=contract_bd.code_contract)
        temperature_bd = TemperatureSensors.objects.filter(device=device_bd.device_id)
        energy_bd = EnergySensors.objects.filter(device=device_bd.device_id)
        voice_bd = VoiceSensors.objects.filter(device=device_bd.device_id)
        light_bd = LightSensors.objects.filter(device=device_bd.device_id)
        favorite_temperature_bd = TemperatureSensors.objects.filter(device=device_bd.device_id, favorite=1)
        favorite_energy_bd = EnergySensors.objects.filter(device=device_bd.device_id, favorite=1)
        favorite_voice_bd = VoiceSensors.objects.filter(device=device_bd.device_id, favorite=1)
        favorite_light_bd = LightSensors.objects.filter(device=device_bd.device_id, favorite=1)
        contract_serializer = ContractsSerializer(contract_bd)
        address_serializer = AddressesSerializer(address_bd)
        device_serializer = DevicesSerializer(device_bd)
        temperature_serializer = TemperatureSensorsSerializer(temperature_bd, many=True)
        energy_serializer = EnergySensorsSerializer(energy_bd, many=True)
        voice_serializer = VoiceSensorsSerializer(voice_bd, many=True)
        light_serializer = LightSensorsSerializer(light_bd, many=True)
        favorit_temperature_serializer = TemperatureSensorsSerializer(favorite_temperature_bd, many=True)
        favorit_energy_serializer = EnergySensorsSerializer(favorite_energy_bd, many=True)
        favorit_voice_serializer = VoiceSensorsSerializer(favorite_voice_bd, many=True)
        favorit_light_serializer = LightSensorsSerializer(favorite_light_bd, many=True)
        energy = energy_serializer.data
        voice = voice_serializer.data
        light = light_serializer.data
        temperature = temperature_serializer.data
        contract = contract_serializer.data
        address = address_serializer.data
        device = device_serializer.data
        favorit_voice = favorit_voice_serializer.data
        favorit_temperature = favorit_temperature_serializer.data
        favorit_energy = favorit_energy_serializer.data
        favorit_light = favorit_light_serializer.data
        count_con = contract_count
        contract_info = {
            'type': count_con,
            'device': device,
            'address': address,
            'light': light,
            'temp': temperature,
            'energy': energy,
            'voice': voice,
            'fvoice': favorit_voice,
            'flight': favorit_light,
            'fenergy': favorit_energy,
            'ftemp': favorit_temperature,
            'contract': contract
        }
    else:
        count_con = contract_count
        contract_info = {}
        for a in count:
            contract_bd = Contracts.objects.get(code_contract=a.code_contract, archive=0)
            address_bd = Addresses.objects.get(code_contract=a.code_contract)
            device_bd = Devices.objects.get(contract_code=a.code_contract)
            temperature_bd = TemperatureSensors.objects.filter(device=device_bd.device_id)
            energy_bd = EnergySensors.objects.filter(device=device_bd.device_id)
            voice_bd = VoiceSensors.objects.filter(device=device_bd.device_id)
            light_bd = LightSensors.objects.filter(device=device_bd.device_id)
            favorite_temperature_bd = TemperatureSensors.objects.filter(device=device_bd.device_id, favorite=1)
            favorite_energy_bd = EnergySensors.objects.filter(device=device_bd.device_id, favorite=1)
            favorite_voice_bd = VoiceSensors.objects.filter(device=device_bd.device_id, favorite=1)
            favorite_light_bd = LightSensors.objects.filter(device=device_bd.device_id, favorite=1)
            contract_serializer = ContractsSerializer(contract_bd)
            address_serializer = AddressesSerializer(address_bd)
            device_serializer = DevicesSerializer(device_bd)
            temperature_serializer = TemperatureSensorsSerializer(temperature_bd, many=True)
            energy_serializer = EnergySensorsSerializer(energy_bd, many=True)
            voice_serializer = VoiceSensorsSerializer(voice_bd, many=True)
            light_serializer = LightSensorsSerializer(light_bd, many=True)
            favorit_temperature_serializer = TemperatureSensorsSerializer(favorite_temperature_bd, many=True)
            favorit_energy_serializer = EnergySensorsSerializer(favorite_energy_bd, many=True)
            favorit_voice_serializer = VoiceSensorsSerializer(favorite_voice_bd, many=True)
            favorit_light_serializer = LightSensorsSerializer(favorite_light_bd, many=True)
            energy = energy_serializer.data
            voice = voice_serializer.data
            light = light_serializer.data
            temperature = temperature_serializer.data
            contract = contract_serializer.data
            address = address_serializer.data
            device = device_serializer.data
            favorit_voice = favorit_voice_serializer.data
            favorit_temperature = favorit_temperature_serializer.data
            favorit_energy = favorit_energy_serializer.data
            favorit_light = favorit_light_serializer.data
            contract_info[a.code_contract] = {
                'type': count_con,
                'device': device,
                'address': address,
                'light': light,
                'temp': temperature,
                'energy': energy,
                'voice': voice,
                'fvoice': favorit_voice,
                'flight': favorit_light,
                'fenergy': favorit_energy,
                'ftemp': favorit_temperature,
                'contract': contract
            }
    report_serializer = ReportSensorsParamsSerializer(reports, many=True)
    report = report_serializer.data
    client_serializer = ClientsSerializer(cl)
    client = client_serializer.data
    settings_serializer = UserSettingsSerializer(settings)
    setting = settings_serializer.data
    notifications_serializer = NotificationsSerializer(notifications, many=True)
    notification = notifications_serializer.data
    alls = {'client': client, 'setting': setting, 'report': report, 'notification': notification,
            'contract': contract_info, 'count': count_con}
    return JsonResponse(alls)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_panel')
            else:
                ids = User.objects.get(username=user)
                idd = ids.id
                client = Clients.objects.get(user_id=idd)
                archcontr = Contracts.objects.filter(archive=1, client=client)
                unarchcontr = Contracts.objects.filter(archive=0, client=client)
                if archcontr and unarchcontr:
                    return redirect('cabinet')
                elif archcontr and not unarchcontr:
                    error_message = 'Ваш договор заморожен, обратитесь в поддержку за дополнительной информацией'
                    return render(request, 'main/lg.html', {'error_message': error_message})
                elif not archcontr and unarchcontr:
                    return redirect('cabinet')
                elif not archcontr and not unarchcontr:
                    error_message = 'На данном аккаунте нет договоров'
                    return render(request, 'main/lg.html', {'error_message': error_message})
        else:
            error_message = 'Неправильный логин или пароль'
            return render(request, 'main/lg.html', {'error_message': error_message})
    else:
        return render(request, 'main/lg.html')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def support(request):
    return render(request, 'main/support.html')


def send_email_view(request):
    if request.method == 'POST':
        user = request.user
        client = user.clients
        email = client.email
        contr = Contracts.objects.get(client=client)
        date = datetime.now()
        frm = date.strftime("%d.%m.%Y %H:%M")
        message = 'Оплата услуг прошла успешно!'

        context = {'message': message, 'frm': frm, 'em': email}
        html_message = render_to_string('main/email_template.html', context)

        send_mail(
            'Оплата услуг(квитанция)',
            message,
            'housecloudufa@gmail.com',
            [email],
            html_message=html_message,
            fail_silently=False,
        )
        contr.contract_payment = one_month_later
        contr.save()
        return JsonResponse({'status': f'Successfully sent email'})
    else:
        return JsonResponse({'status': 'No sent email'})


def logout_view(request):
    logout(request)
    return redirect('home')


def notification_send(request):
    if request.method == 'POST':
        user = request.user
        client = user.clients
        contr = Contracts.objects.get(client=client)
        dev = Devices.objects.get(contract_code=contr)
        voice = VoiceSensors.objects.filter(device=dev)
        energy = EnergySensors.objects.filter(device=dev)
        temp = TemperatureSensors.objects.filter(device=dev)
        notifications_sent = 0
        if dev.status == "Активно":
            for Vsensor in voice:
                if Vsensor.voice_max < Vsensor.voice_result:
                    val = Vsensor.voice_result - Vsensor.voice_max
                    Notifications.objects.create(user_id=user, notification_type="Тревога",
                                                 notification_description=f"Сенсор {Vsensor.description} зафиксировал превышение порога звука на {val}Db",
                                                 notification_date=date_notif)
                    ReportSensorsParams.objects.create(user_id=user, voice_id=Vsensor.sensor_id,
                                                       int_param=Vsensor.voice_result, date_param=datee,
                                                       time_param=timee,
                                                       type_sensor="ЗвукUp")

                    notifications_sent += 1
            for Esensor in energy:
                if Esensor.max_voltage < Esensor.sensor_result_voltage:
                    volt = Esensor.sensor_result_voltage - Esensor.max_voltage
                    Notifications.objects.create(user_id=user, notification_type="Тревога",
                                                 notification_description=f"Сенсор {Esensor.description} зафиксировал скачок напряжения на {volt}V",
                                                 notification_date=date_notif)
                    ReportSensorsParams.objects.create(user_id=user, energy_id=Esensor.sensor_id,
                                                       int_param=Esensor.sensor_result_voltage, date_param=datee,
                                                       time_param=timee,
                                                       float_param=Esensor.sensor_result_energy,
                                                       type_sensor="ЭлектричествоUp")

                    notifications_sent += 1
                elif Esensor.min_voltage > Esensor.sensor_result_voltage:
                    Notifications.objects.create(user_id=user, notification_type="Тревога",
                                                 notification_description=f"Сенсор {Esensor.description} зафиксировал утечку напряжения, порог напряжения перешел минимум {Esensor.min_voltage}V",
                                                 notification_date=date_notif)
                    ReportSensorsParams.objects.create(user_id=user, energy_id=Esensor.sensor_id,
                                                       int_param=Esensor.sensor_result_voltage,
                                                       float_param=Esensor.sensor_result_energy, date_param=datee,
                                                       time_param=timee,
                                                       type_sensor="ЭлектричествоDown")

                    notifications_sent += 1
            for Tsensor in temp:
                if Tsensor.max_temperature < Tsensor.temperature_result:
                    val = Tsensor.temperature_result - Tsensor.max_temperature
                    Notifications.objects.create(user_id=user, notification_type="Предупреждение",
                                                 notification_description=f"Сенсор {Tsensor.description} зафиксировал повышение порога температуры на {val}°C",
                                                 notification_date=date_notif)
                    ReportSensorsParams.objects.create(user_id=user, temp_id=Tsensor.sensor_id,
                                                       int_param=Tsensor.temperature_result, date_param=datee,
                                                       time_param=timee,
                                                       type_sensor="ТемператураUp")
                    notifications_sent += 1
                elif Tsensor.min_temperature > Tsensor.temperature_result:
                    valm = Tsensor.min_temperature - Tsensor.temperature_result
                    Notifications.objects.create(user_id=user, notification_type="Предупреждение",
                                                 notification_description=f"Сенсор {Tsensor.description} зафиксировал понижение порога температуры на {valm}°C",
                                                 notification_date=date_notif)
                    ReportSensorsParams.objects.create(user_id=user, temp_id=Tsensor.sensor_id,
                                                       int_param=Tsensor.temperature_result, date_param=datee,
                                                       time_param=timee,
                                                       type_sensor="ТемператураDown")
                    notifications_sent += 1
        if notifications_sent > 0:
            return JsonResponse({'status': f'Successfully sent {notifications_sent} notifications'})
        else:
            return JsonResponse({'status': 'No notifications sent'})


def clear_notif_all(request):
    if request.method == 'POST':
        user_id = request.user.id
        notifications = Notifications.objects.filter(user_id=user_id)
        notifications.delete()
        return JsonResponse({'status': True})


def clear_notif(request):
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        user_id = request.user.id
        notification = Notifications.objects.get(notification_id=notification_id, user_id=user_id)
        notification.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def accept_settings_upd(request):
    if request.method == 'POST':
        senname = request.POST.get('sname')
        minrr = request.POST.get('rmin')
        maxrr = request.POST.get('rmax')
        minr = int(minrr)
        maxr = int(maxrr)
        user = request.user
        client = user.clients
        contr = Contracts.objects.get(client=client)
        dev = Devices.objects.get(contract_code=contr)
        voice = VoiceSensors.objects.filter(device=dev, sensor_name=senname).first()
        energy = EnergySensors.objects.filter(device=dev, sensor_name=senname).first()
        temp = TemperatureSensors.objects.filter(device=dev, sensor_name=senname).first()
        if voice is not None:
            b = abs(maxr)
            a = abs(minr)
            voice.voice_min = a
            voice.voice_max = b
            voice.save()
            return JsonResponse({'success': True})
        elif energy is not None:
            a = abs(minr)
            b = abs(maxr)
            energy.min_voltage = a
            energy.max_voltage = b
            energy.save()
            return JsonResponse({'success': True})
        elif temp is not None:
            b = abs(maxr)
            temp.min_temperature = minr
            temp.max_temperature = b
            temp.save()
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def settings_acc(request):
    if request.method == 'POST':
        s1 = request.POST.get('spd1')
        s2 = request.POST.get('spd2')
        s3 = request.POST.get('spd3')
        user = request.user
        setting = UserSettings.objects.get(user=user)
        if s1 == "true":
            if setting.time_sensors != 1:
                setting.time_sensors = 1
                setting.save()
                return JsonResponse({'success': True})
        elif s2 == "true":
            if setting.time_sensors != 2:
                setting.time_sensors = 2
                setting.save()
                return JsonResponse({'success': True})
        elif s3 == "true":
            if setting.time_sensors != 3:
                setting.time_sensors = 3
                setting.save()
                return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Нет изменений'})
    else:
        return JsonResponse({'success': False})


def favorite_add(request):
    if request.method == 'POST':
        sens = request.POST.get('sens_id')
        sens_type = request.POST.get('sens_type')
        if sens_type == 'Электричество':
            sensor = EnergySensors.objects.get(sensor_id=sens)
        elif sens_type == 'Звук':
            sensor = VoiceSensors.objects.get(sensor_id=sens)
        elif sens_type == 'Температура':
            sensor = TemperatureSensors.objects.get(sensor_id=sens)
        elif sens_type == 'Свет':
            sensor = LightSensors.objects.get(sensor_id=sens)
        else:
            return HttpResponseBadRequest('Invalid sensor_id')

        if sensor.favorite == 0:
            sensor.favorite = 1
            sensor.save()
        else:
            sensor.favorite = 0
            sensor.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


def device_button_on(request):
    if request.method == 'POST':
        user = request.user
        sett = UserSettings.objects.get(user_id=user)
        client = user.clients
        contr = Contracts.objects.get(client=client)
        dev = Devices.objects.get(contract_code=contr)
        if sett.device_start_stop == 0:
            sett.device_start_stop = 1
            dev.status = "Активно"
            Notifications.objects.create(user_id=user, notification_type="Успешно",
                                         notification_description=f"Устройство {dev.device_name} включено",
                                         notification_date=date_notif)
        sett.save()
        dev.save()
        return JsonResponse({'status': 'success'})


def light_onoff(request):
    if request.method == 'POST':
        sens = request.POST.get('sens_id')
        user = request.user
        client = user.clients
        contr = Contracts.objects.get(client=client)
        dev = Devices.objects.get(contract_code=contr)
        ss = LightSensors.objects.get(sensor_id=sens, device_id=dev)
        if ss.light_result == 0:
            ss.light_result = 1
        else:
            ss.light_result = 0
        ss.save()
        return HttpResponse()
    else:
        return JsonResponse({'status': 'error'})


def active_device(request):
    central_unit = body.CentralUnit()
    central_unit.send_sensor_data_to_mysql()
    return JsonResponse({'status': 'success'})


def device_button_off(request):
    if request.method == 'POST':
        user = request.user
        sett = UserSettings.objects.get(user_id=user)
        client = user.clients
        contr = Contracts.objects.get(client=client)
        dev = Devices.objects.get(contract_code=contr)
        if sett.device_start_stop == 1:
            sett.device_start_stop = 0
            dev.status = "Неактивно"
            Notifications.objects.create(user_id=user, notification_type="Предупреждение",
                                         notification_description=f"Устройство {dev.device_name} выключено",
                                         notification_date=date_notif)

        sett.save()
        dev.save()
        return JsonResponse({'status': 'success'})


import locale


def report_sens(request):
    if request.method == 'POST':
        T = request.POST.get('temprep')
        E = request.POST.get('energyrep')
        V = request.POST.get('voicerep')
        locale.setlocale(locale.LC_TIME, 'ru_RU')
        date_start = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
        date_end = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
        start = date_start.strftime('%d %B %Y').lstrip("0").replace(" 0", " ")
        end = date_end.strftime('%d %B %Y').lstrip("0").replace(" 0", " ")
        user = request.user
        client = user.clients
        contr = Contracts.objects.get(client=client)
        dev = Devices.objects.get(contract_code=contr)
        voice = VoiceSensors.objects.filter(device=dev)
        energy = EnergySensors.objects.filter(device=dev)
        temp = TemperatureSensors.objects.filter(device=dev)
        reportT = ReportSensorsParams.objects.filter(
            Q(user_id=user) & Q(date_param__gte=date_start) & Q(date_param__lte=date_end) &
            (Q(type_sensor='ТемператураUp') | Q(type_sensor='ТемператураDown'))
        )
        reportE = ReportSensorsParams.objects.filter(
            Q(user_id=user) & Q(date_param__gte=date_start) & Q(date_param__lte=date_end) &
            (Q(type_sensor='ЭлектричествоUp') | Q(type_sensor='ЭлектричествоDown'))
        )
        reportV = ReportSensorsParams.objects.filter(
            Q(user_id=user) & Q(date_param__gte=date_start) & Q(date_param__lte=date_end) &
            (Q(type_sensor='ЗвукUp') | Q(type_sensor='ЗвукDown'))
        )
        if T == "true" and E == "false" and V == "false":
            context = {'reportV': None, 'reportE': None, 'reportT': reportT, 'temp': temp, 'energy': energy,
                       'voice': voice, 'start': start, 'end': end}
        elif T == "false" and E == "true" and V == "false":
            context = {'reportV': None, 'reportE': reportE, 'reportT': None, 'temp': temp, 'energy': energy,
                       'voice': voice, 'start': start, 'end': end}
        elif T == "false" and E == "false" and V == "true":
            context = {'reportV': reportV, 'reportE': None, 'reportT': None, 'temp': temp, 'energy': energy,
                       'voice': voice, 'start': start, 'end': end}
        elif T == "true" and E == "true" and V == "false":
            context = {'reportV': None, 'reportE': reportE, 'reportT': reportT, 'temp': temp, 'energy': energy,
                       'voice': voice, 'start': start, 'end': end}
        elif T == "true" and E == "false" and V == "true":
            context = {'reportV': reportV, 'reportE': None, 'reportT': reportT, 'temp': temp, 'energy': energy,
                       'voice': voice, 'start': start, 'end': end}
        elif T == "false" and E == "true" and V == "true":
            context = {'reportV': reportV, 'reportE': reportE, 'reportT': None, 'temp': temp, 'energy': energy,
                       'voice': voice, 'start': start, 'end': end}
        else:
            context = {'reportV': reportV, 'reportE': reportE, 'reportT': reportT, 'temp': temp, 'energy': energy,
                       'voice': voice, 'start': start, 'end': end}

        html = render_to_string('main/report_template.html', context)
        response = HttpResponse(html, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="report.html"'
        return response
    else:
        return JsonResponse({'status': 'error'})


def report_sens_all(request):
    if request.method == 'POST':
        locale.setlocale(locale.LC_TIME, 'ru_RU')
        date_start = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d').date()
        date_end = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d').date()
        start = date_start.strftime('%d %B %Y').lstrip("0").replace(" 0", " ")
        end = date_end.strftime('%d %B %Y').lstrip("0").replace(" 0", " ")
        user = request.user
        client = user.clients
        contr = Contracts.objects.get(client=client)
        dev = Devices.objects.get(contract_code=contr)
        voice = VoiceSensors.objects.filter(device=dev)
        energy = EnergySensors.objects.filter(device=dev)
        temp = TemperatureSensors.objects.filter(device=dev)
        reportT = ReportSensorsParams.objects.filter(
            Q(user_id=user) & Q(date_param__gte=date_start) & Q(date_param__lte=date_end) &
            (Q(type_sensor='ТемператураUp') | Q(type_sensor='ТемператураDown'))
        )
        reportE = ReportSensorsParams.objects.filter(
            Q(user_id=user) & Q(date_param__gte=date_start) & Q(date_param__lte=date_end) &
            (Q(type_sensor='ЭлектричествоUp') | Q(type_sensor='ЭлектричествоDown'))
        )
        reportV = ReportSensorsParams.objects.filter(
            Q(user_id=user) & Q(date_param__gte=date_start) & Q(date_param__lte=date_end) &
            (Q(type_sensor='ЗвукUp') | Q(type_sensor='ЗвукDown'))
        )

        context = {'reportV': reportV, 'reportE': reportE, 'reportT': reportT, 'temp': temp, 'energy': energy,
                   'voice': voice, 'start': start, 'end': end}
        html = render_to_string('main/report_template.html', context)
        response = HttpResponse(html, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="report.html"'
        return response
    else:
        return JsonResponse({'status': 'error'})


def search_admin(request):
    username = request.user.username
    query = request.GET.get('query')
    date = request.GET.get('filter')
    contracts = Contracts.objects.all()

    if query:
        contracts = contracts.filter(
            Q(client__name__icontains=query) |
            Q(client__surname__icontains=query) |
            Q(client__patronymic__icontains=query) |
            Q(code_contract__icontains=query)
        )

    if date == 'Сегодня':
        contracts = contracts.filter(contract_start=datee)

    if date == 'За этот год':
        current_year = datee.today().year
        contracts = contracts.filter(contract_start__year=current_year)

    if date == 'За этот месяц':
        contracts = Contracts.objects.filter(contract_start__year=datee.year, contract_start__month=datee.month)

    if date == 'Последние 7дней':
        week_ago = datee - timedelta(days=7)
        contracts = Contracts.objects.filter(contract_start__range=[week_ago, datee])

    context = {
        'contract': contracts, 'username': username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin2(request):
    username = request.user.username
    query = request.GET.get('query')
    client = Clients.objects.all()

    if query:
        client = client.filter(
            Q(name__icontains=query) |
            Q(surname__icontains=query) |
            Q(patronymic__icontains=query)
        )

    context = {
        'client': client,'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin3(request):
    username = request.user.username
    query = request.GET.get('query')
    dev = Devices.objects.all()

    if query:
        dev = dev.filter(
            Q(contract_code__code_contract__icontains=query) |
            Q(device_name__icontains=query) |
            Q(ip__icontains=query) | Q(status__icontains=query)
        )

    context = {
        'device': dev, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin4(request):
    username = request.user.username
    query = request.GET.get('query')
    sens = TemperatureSensors.objects.all()

    if query:
        sens = sens.filter(
            Q(device__device_name__icontains=query) |
            Q(sensor_name__icontains=query)
        )

    context = {
        'temp': sens, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin5(request):
    username = request.user.username
    query = request.GET.get('query')
    sens = EnergySensors.objects.all()

    if query:
        sens = sens.filter(
            Q(device__device_name__icontains=query) |
            Q(sensor_name__icontains=query)
        )

    context = {
        'energy': sens, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin6(request):
    username = request.user.username
    query = request.GET.get('query')
    sens = VoiceSensors.objects.all()

    if query:
        sens = sens.filter(
            Q(device__device_name__icontains=query) |
            Q(sensor_name__icontains=query)
        )

    context = {
        'voice': sens, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin7(request):
    username = request.user.username
    query = request.GET.get('query')
    sens = LightSensors.objects.all()

    if query:
        sens = sens.filter(
            Q(device__device_name__icontains=query) |
            Q(sensor_name__icontains=query)
        )

    context = {
        'light': sens, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin8(request):
    username = request.user.username
    query = request.GET.get('query')
    al = Notifications.objects.all()

    if query:
        al = al.filter(
            Q(user_id__username__icontains=query) |
            Q(notification_type__icontains=query)
        )

    context = {
        'notification': al, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin9(request):
    username = request.user.username
    query = request.GET.get('query')
    al = UserSettings.objects.all()

    if query:
        al = al.filter(user_id__username__icontains=query)

    context = {
        'settings': al, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin10(request):
    username = request.user.username
    query = request.GET.get('query')
    al = Addresses.objects.all()

    if query:
        al = al.filter(code_contract__code_contract__icontains=query)

    context = {
        'address': al, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


def search_admin11(request):
    username = request.user.username
    query = request.GET.get('query')
    al = ReportSensorsParams.objects.all()

    if query:
        al = al.filter(user_id__username__icontains=query)
    context = {
        'report': al, 'username':username
    }

    return render(request, 'main/adminpanel.html', context)


@require_POST
def delete_admin_temp(request):
    ids = request.POST.getlist('ids[]')
    for id in ids:
        temp = get_object_or_404(TemperatureSensors, pk=id)
        reps = ReportSensorsParams.objects.filter(temp=id)
        fav = Favorites.objects.filter(temp_sensor=id)
        reps.delete()
        fav.delete()
        temp.delete()
    return JsonResponse({'success': True})


@require_POST
def delete_admin_light(request):
    ids = request.POST.getlist('ids[]')
    for id in ids:
        l = get_object_or_404(LightSensors, pk=id)
        fav = Favorites.objects.filter(light_sensor=id)
        fav.delete()
        l.delete()
    return JsonResponse({'success': True})


@require_POST
def delete_admin_energy(request):
    ids = request.POST.getlist('ids[]')
    for id in ids:
        e = get_object_or_404(EnergySensors, pk=id)
        reps = ReportSensorsParams.objects.filter(energy=id)
        fav = Favorites.objects.filter(energy_sensor=id)
        reps.delete()
        fav.delete()
        e.delete()
    return JsonResponse({'success': True})


@require_POST
def delete_admin_notif(request):
    ids = request.POST.getlist('idsn[]')
    for id in ids:
        e = get_object_or_404(Notifications, pk=id)
        e.delete()
    return JsonResponse({'success': True})


@require_POST
def delete_admin_report(request):
    ids = request.POST.getlist('idsr[]')
    for id in ids:
        e = get_object_or_404(ReportSensorsParams, pk=id)
        e.delete()
    return JsonResponse({'success': True})


@require_POST
def delete_admin_voice(request):
    ids = request.POST.getlist('ids[]')
    for id in ids:
        v = get_object_or_404(VoiceSensors, pk=id)
        reps = ReportSensorsParams.objects.filter(voice=id)
        fav = Favorites.objects.filter(voice_sensor=id)
        reps.delete()
        fav.delete()
        v.delete()
    return JsonResponse({'success': True})


def update_admin_temp(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        minTemperature = request.POST.get('minTemperature')
        maxTemperature = request.POST.get('maxTemperature')
        min_temperature = minTemperature.replace("°C", "")
        max_temperature = maxTemperature.replace("°C", "")
        desc = request.POST.get('description')
        temp = TemperatureSensors.objects.get(sensor_id=id)
        temp.description = desc
        temp.min_temperature = min_temperature
        temp.max_temperature = max_temperature
        temp.save()
        return JsonResponse({'status': 'Yes update'})
    else:
        return JsonResponse({'status': 'No update'})


import re


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)


def is_valid_phone(phone):
    phone_regex = r'^8\d{10}$'
    return re.match(phone_regex, phone)


def validate_address(address):
    pattern = r'^[А-Яа-я0-9\s.,/-]+$'
    return re.match(pattern, address)


def update_admin_client(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        if not is_valid_email(email):
            return JsonResponse({'status': 'Неправильный Email'}, status=400)

        if not is_valid_phone(mobile):
            return JsonResponse({'status': 'Неправильный номер'}, status=400)
        client = Clients.objects.get(client_id=id)
        client.name = name
        client.surname = surname
        client.patronymic = patronymic
        client.mobile = mobile
        client.email = email
        contract = get_object_or_404(Contracts, client=client)
        current_date = datetime.now()
        one_month_later = current_date + timedelta(days=30)
        contract.contract_start = current_date
        contract.contract_payment = one_month_later
        contract.save()
        client.save()
        return JsonResponse({'status': 'Yes update'})
    else:
        return JsonResponse({'status': 'Ошибка обновления данных...'}, status=405)


def update_admin_voice(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        min = request.POST.get('minVoice')
        max = request.POST.get('maxVoice')
        min_voice = min.replace("Db", "")
        max_voice = max.replace("Db", "")
        desc = request.POST.get('description')
        voice = VoiceSensors.objects.get(sensor_id=id)
        voice.description = desc
        voice.voice_min = min_voice
        voice.voice_max = max_voice
        voice.save()
        return JsonResponse({'status': 'Yes update'})
    else:
        return JsonResponse({'status': 'No update'})


def update_admin_light(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        desc = request.POST.get('description')
        light = LightSensors.objects.get(sensor_id=id)
        light.description = desc
        light.save()
        return JsonResponse({'status': 'Yes update'})
    else:
        return JsonResponse({'status': 'No update'})


def update_admin_energy(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        mine = request.POST.get('minEnergy')
        maxe = request.POST.get('maxEnergy')
        minv = request.POST.get('minVoltage')
        maxv = request.POST.get('maxVoltage')
        minn_energy = mine.replace("КлВт/ч", "")
        maxx_energy = maxe.replace("КлВт/ч", "")
        max_energy_value = maxx_energy.replace(',', '.')
        max_energy = float(max_energy_value)
        min_energy_value = minn_energy.replace(',', '.')
        min_energy = float(min_energy_value)
        min_voltage = minv.replace("V", "")
        max_voltage = maxv.replace("V", "")
        desc = request.POST.get('description')
        energy = EnergySensors.objects.get(sensor_id=id)
        energy.description = desc
        energy.min_energy = min_energy
        energy.max_energy = max_energy
        energy.max_voltage = max_voltage
        energy.min_voltage = min_voltage
        energy.save()
        return JsonResponse({'status': 'Yes update'})
    else:
        return JsonResponse({'status': 'No update'})


def add_admin_temp(request):
    if request.method == 'POST':
        device_code = int(request.POST.get('deviceCodetemp'))
        sensorName = request.POST.get('sensorName')
        ip = request.POST.get('ip')
        location = request.POST.get('location')
        minThreshold = request.POST.get('minThreshold')
        maxThreshold = request.POST.get('maxThreshold')
        if not sensorName or not ip:
            error_message = 'Наименование и ip обязательны для заполнения'
            return JsonResponse({'status': 'error', 'message': error_message})
        if TemperatureSensors.objects.filter(ip=ip).exists():
            error_message = 'Датчик с таким ip уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        if TemperatureSensors.objects.filter(sensor_name=sensorName).exists():
            error_message = 'Датчик с таким названием уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        if minThreshold == '':
            minn = 0
        else:
            minn = int(minThreshold)

        if maxThreshold == '':
            maxx = 0
        else:
            maxx = int(maxThreshold)
        device = Devices.objects.get(device_id=device_code)
        TemperatureSensors.objects.create(device=device, sensor_name=sensorName, description=location,
                                          max_temperature=maxx, ip=ip, min_temperature=minn, sensor_type="Температура",
                                          favorite=0)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def add_admin_voice(request):
    if request.method == 'POST':
        device_code = int(request.POST.get('deviceCodevoice'))
        sensorName = request.POST.get('sensorName')
        ip = request.POST.get('ip')
        location = request.POST.get('location')
        minThreshold = request.POST.get('minThreshold')
        maxThreshold = request.POST.get('maxThreshold')
        if not sensorName or not ip:
            error_message = 'Наименование и ip обязательны для заполнения'
            return JsonResponse({'status': 'error', 'message': error_message})
        if VoiceSensors.objects.filter(ip=ip).exists():
            error_message = 'Датчик с таким ip уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        if VoiceSensors.objects.filter(sensor_name=sensorName).exists():
            error_message = 'Датчик с таким названием уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        if minThreshold == '':
            minn = 0
        else:
            minn = int(minThreshold)

        if maxThreshold == '':
            maxx = 0
        else:
            maxx = int(maxThreshold)
        device = Devices.objects.get(device_id=device_code)
        VoiceSensors.objects.create(device=device, sensor_name=sensorName, ip=ip, description=location,
                                    sensor_type="Звук", voice_max=maxx,
                                    voice_min=minn, favorite=0)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def add_admin_light(request):
    if request.method == 'POST':
        device_code = int(request.POST.get('deviceCodelight'))
        sensorName = request.POST.get('sensorName')
        ip = request.POST.get('ip')
        location = request.POST.get('location')
        if not sensorName or not ip:
            error_message = 'Наименование и ip обязательны для заполнения'
            return JsonResponse({'status': 'error', 'message': error_message})
        if LightSensors.objects.filter(ip=ip).exists():
            error_message = 'Датчик с таким ip уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        if LightSensors.objects.filter(sensor_name=sensorName).exists():
            error_message = 'Датчик с таким названием уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        device = Devices.objects.get(device_id=device_code)
        LightSensors.objects.create(device=device, sensor_name=sensorName, ip=ip, description=location,
                                    sensor_type="Свет", light_result=0,
                                    favorite=0)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def add_admin_energy(request):
    if request.method == 'POST':
        device_code = int(request.POST.get('deviceCodeenergy'))
        sensorName = request.POST.get('sensorName')
        location = request.POST.get('location')
        minThresholde = request.POST.get('minThresholde')
        maxThresholde = request.POST.get('maxThresholde')
        minThresholdv = request.POST.get('minThresholdv')
        maxThresholdv = request.POST.get('maxThresholdv')
        ip = request.POST.get('ip')
        if not sensorName or not ip:
            error_message = 'Наименование и ip обязательны для заполнения'
            return JsonResponse({'status': 'error', 'message': error_message})
        if EnergySensors.objects.filter(ip=ip).exists():
            error_message = 'Датчик с таким ip уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        if EnergySensors.objects.filter(sensor_name=sensorName).exists():
            error_message = 'Датчик с таким названием уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})
        if minThresholde == '':
            mine = 0
        else:
            mine = int(minThresholde)

        if maxThresholde == '':
            maxe = 0
        else:
            maxe = int(maxThresholde)

        if minThresholdv == '':
            minv = 0
        else:
            minv = int(minThresholdv)

        if maxThresholdv == '':
            maxv = 0
        else:
            maxv = int(maxThresholdv)
        device = Devices.objects.get(device_id=device_code)
        EnergySensors.objects.create(device=device, sensor_name=sensorName, ip=ip, sensor_type="Электричество",
                                     description=location, max_energy=maxe,
                                     min_energy=mine, max_voltage=maxv, min_voltage=minv, favorite=0)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


from django.contrib.auth.models import Group


def create_admin_contract(request):
    if request.method == 'POST':
        name = request.POST.get('firstName')
        surname = request.POST.get('lastName')
        patronymic = request.POST.get('middleName')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        email = request.POST.get('email')
        login = request.POST.get('login')
        password = request.POST.get('password')
        deviceName = request.POST.get('deviceName')
        ipAddress = request.POST.get('ipAddress')

        valid_logins = ["admin", "root", "administrator", "test", "superuser", "su"]
        if login.lower() in valid_logins:
            error_message = 'Недопустимый логин'
            return JsonResponse({'status': 'error', 'message': error_message})

        if User.objects.filter(username=login).exists():
            error_message = 'Пользователь с таким логином уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Clients.objects.filter(email=email).exists():
            error_message = 'Клиент с таким Email уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Clients.objects.filter(mobile=phone).exists():
            error_message = 'Клиент с таким телефоном уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Addresses.objects.filter(address=address).exists():
            error_message = 'Клиент с таким адресом уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Devices.objects.filter(device_name=deviceName).exists():
            error_message = 'Устройство с таким названием уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Devices.objects.filter(ip=ipAddress).exists():
            error_message = 'Устройство с таким ip уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if not is_valid_email(email):
            error_message = 'Некорректный email'
            return JsonResponse({'status': 'error', 'message': error_message})

        if not is_valid_phone(phone):
            error_message = 'Некорректный номер телефона'
            return JsonResponse({'status': 'error', 'message': error_message})

        if not validate_address(address):
            error_message = 'Некорректный адрес'
            return JsonResponse({'status': 'error', 'message': error_message})

        user = User(username=login)
        user.set_password(password)
        user.save()

        group = Group.objects.get(name='Client')
        group.user_set.add(user)

        client = Clients.objects.create(user_id=user, name=name, surname=surname, patronymic=patronymic,
                                        mobile=phone, email=email, uncpass=password)

        current_date = datetime.now()
        one_month_later = current_date + timedelta(days=30)

        contractt = Contracts.objects.create(client=client, contract_start=current_date,
                                             contract_payment=one_month_later, price=500, archive=0)

        Devices.objects.create(contract_code=contractt, device_name=deviceName,
                               device_description="Центральное устройство сбора данных", ip=ipAddress,
                               status="Неактивно")
        Addresses.objects.create(id_client=client, code_contract=contractt, address=address)
        UserSettings.objects.create(user=user, device_start_stop=0, email_message=1, time_sensors=1)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def delete_admin_contract(request):
    if request.method == 'POST':
        contract_id = request.POST.get('contractId')
        contract = Contracts.objects.get(code_contract=contract_id)
        contract.archive = 1
        contract.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def arch_admin_contract(request):
    if request.method == 'POST':
        contract_id = request.POST.get('contractId')
        contract = Contracts.objects.get(code_contract=contract_id)
        contract.archive = 1
        contract.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def unarch_admin_contract(request):
    if request.method == 'POST':
        contract_id = request.POST.get('contractId')
        contract = Contracts.objects.get(code_contract=contract_id)
        contract.archive = 0
        contract.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User


def load_admin_contract(request):
    if request.method == 'POST':
        contract_id = request.POST.get('contractId')
        contract = get_object_or_404(Contracts, code_contract=contract_id)
        client = contract.client
        device = get_object_or_404(Devices, contract_code=contract)
        password = client.uncpass
        userr = client.user_id
        user = get_object_or_404(User, username=userr)
        login = user.username
        adress = Addresses.objects.get(code_contract=contract_id)
        voice = VoiceSensors.objects.filter(device=device)
        energy = EnergySensors.objects.filter(device=device)
        temp = TemperatureSensors.objects.filter(device=device)
        light = LightSensors.objects.filter(device=device)
        addr = adress.address
        context = {
            'login': login,
            'password': password,
            'client': client,
            'contract': contract,
            'address': addr,
            'energy': energy,
            'voice': voice,
            'light': light,
            'temp': temp,
            'device': device
        }

        html = render_to_string('main/contract_template.html', context)
        response = HttpResponse(html, content_type='text/html')
        response['Content-Disposition'] = 'attachment; filename="contract.html"'
        return response
    else:
        return JsonResponse({'status': 'error'})


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Devices, Contracts


def add_contract_admin_device(request):
    if request.method == 'POST':
        contract_code = request.POST.get('contractCode')
        device_name = request.POST.get('deviceName')
        ip_address = request.POST.get('ipAddress')

        if Devices.objects.filter(device_name=device_name).exists():
            error_message = 'Устройство с таким названием уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Devices.objects.filter(ip=ip_address).exists():
            error_message = 'Устройство с таким IP-адресом уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        contract = get_object_or_404(Contracts, code_contract=contract_code)
        current_date = datetime.now()
        one_month_later = current_date + timedelta(days=30)
        contract.contract_start = current_date
        contract.contract_payment = one_month_later
        contract.save()
        Devices.objects.create(contract_code=contract, device_name=device_name,
                               device_description="Центральное устройство сбора данных", ip=ip_address,
                               status="Неактивно")

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def editaddr(request):
    if request.method == 'POST':
        adrid = request.POST.get('id')
        adres = request.POST.get('address')
        adr = Addresses.objects.get(address_id=adrid)
        adr.address = adres
        adr.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})


def morecontract(request):
    if request.method == 'POST':
        contract = request.POST.get('contractid')
        address = request.POST.get('address')
        name = request.POST.get('deviceName')
        ip = request.POST.get('ipAddress')
        current_date = datetime.now()
        one_month_later = current_date + timedelta(days=30)
        if Devices.objects.filter(device_name=name).exists():
            error_message = 'Устройство с таким названием уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Devices.objects.filter(ip=ip).exists():
            error_message = 'Устройство с таким ip уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        if Addresses.objects.filter(address=address).exists():
            error_message = 'Клиент с таким адресом уже существует'
            return JsonResponse({'status': 'error', 'message': error_message})

        lastcon = Contracts.objects.get(code_contract=contract)
        cl = lastcon.client.client_id
        cla = Clients.objects.get(client_id=cl)
        a = Contracts.objects.create(client=cla, contract_start=current_date, contract_payment=one_month_later,
                                     price=500, archive=0)
        aa = Contracts.objects.get(code_contract=a.code_contract)
        Devices.objects.create(contract_code=aa, device_name=name,
                               device_description='Центральное устройство сбора данных', ip=ip, status='Неактивно')
        Addresses.objects.create(id_client=cla, code_contract=aa, address=address)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'No update'})
