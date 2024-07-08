# from django.contrib import admin
# from .models import *
#
#
# admin.site.site_header = 'Административная панель CloudHouse'
# admin.site.site_title = 'Административная панель CloudHouse'
# admin.site.index_title = 'Административная панель CloudHouse'
#
#
# class ContractsAdmin(admin.ModelAdmin):
#     list_display = ("code_contract", "client", "contract_start", "contract_payment", "price")
#     list_display_links = ("code_contract",)
#     search_fields = ("code_contract", "client__surname", "client__name")
#     list_filter = ("contract_start", "contract_payment")
#
#     def client(self, obj):
#         return f"{obj.client.surname} {obj.client.name} {obj.client.patronymic}"
#
#     client.short_description = "Клиент"
#
#
# class ClientsAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'name', 'surname', 'patronymic', 'adress', 'mobile', 'email')
#     list_display_links = ('name',)
#     search_fields = ('user_id', 'name', 'surname', 'patronymic', 'adress', 'mobile', 'email')
#
#
# class DevicesAdmin(admin.ModelAdmin):
#     list_display = ('device_name', 'contract_code', 'ip', 'status')
#     list_filter = ('status',)
#     search_fields = ('device_name', 'contract_code__contract_name')
#     ordering = ('device_id',)
#     fieldsets = (
#         (None, {'fields': ('device_name', 'device_description')}),
#         ('Контракт', {'fields': ('contract_code',)}),
#         ('Сеть', {'fields': ('ip',)}),
#         ('Статус', {'fields': ('status',)}),
#     )
#
#
# class EnergySensorsAdmin(admin.ModelAdmin):
#     list_display = (
#         'sensor_name', 'description', 'ip', 'lastpar_date', 'lastpar_time', 'sensor_result_energy',
#         'sensor_result_voltage',
#         'sensor_type', 'max_energy', 'min_energy', 'max_voltage', 'min_voltage', 'favorite')
#     list_filter = ('device', 'sensor_type', 'favorite')
#     search_fields = ('sensor_name', 'ip', 'sensor_type')
#     ordering = ('sensor_id',)
#
#
# class FavoritesAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'energy_sensor', 'light_sensor', 'voice_sensor', 'temp_sensor')
#
#
# class LightSensorsAdmin(admin.ModelAdmin):
#     list_display = (
#         'sensor_name', 'description', 'ip', 'lastpar_date', 'lastpar_time', 'light_result', 'sensor_type', 'favorite')
#     list_display_links = ('sensor_name',)
#     list_filter = ('sensor_name', 'ip', 'lastpar_date', 'sensor_type', 'favorite')
#     search_fields = ('sensor_name', 'description', 'ip', 'sensor_type', 'favorite')
#
#
# class NotificationsAdmin(admin.ModelAdmin):
#     list_display = ('user_id', 'notification_type', 'notification_description', 'notification_date')
#     list_filter = ('user_id', 'notification_type', 'notification_date')
#     search_fields = ('user_id__username', 'notification_type', 'notification_description')
#     ordering = ('-notification_date',)
#
#
# class ReportSensorsParamsAdmin(admin.ModelAdmin):
#     list_display = ['report_sensors_params_id', 'user_id', 'energy', 'temp', 'voice', 'light', 'float_param',
#                     'bool_param', 'int_param', 'date_param', 'time_param', 'type_sensor']
#     list_filter = ['user_id', 'energy', 'temp', 'voice', 'light', 'type_sensor']
#     search_fields = ['report_sensors_params_id', 'user_id__username', 'energy__sensor_name', 'temp__sensor_name',
#                      'voice__sensor_name', 'light__sensor_name']
#
#
# class TemperatureSensorsAdmin(admin.ModelAdmin):
#     list_display = ('device', 'sensor_name', 'ip', 'lastpar_date', 'lastpar_time', 'temperature_result', 'favorite')
#     list_filter = ('device', 'sensor_type', 'favorite')
#     search_fields = ('sensor_name', 'description')
#
#
# class UserSettingsAdmin(admin.ModelAdmin):
#     list_display = ['user', 'device_start_stop', 'email_message', 'time_sensors']
#     list_filter = ['device_start_stop', 'email_message', 'time_sensors']
#     search_fields = ['user__username', 'user__first_name', 'user__last_name']
#
#
# class VoiceSensorsAdmin(admin.ModelAdmin):
#     list_display = (
#         'device', 'sensor_name', 'description', 'ip', 'lastpar_date', 'lastpar_time', 'voice_result', 'sensor_type',
#         'voice_min', 'voice_max', 'favorite')
#     list_filter = ('device', 'sensor_type')
#     search_fields = ('sensor_name', 'description', 'ip')
#
#
# admin.site.register(ReportSensorsParams, ReportSensorsParamsAdmin)
# admin.site.register(TemperatureSensors, TemperatureSensorsAdmin)
# admin.site.register(Clients, ClientsAdmin)
# admin.site.register(Contracts, ContractsAdmin)
# admin.site.register(VoiceSensors, VoiceSensorsAdmin)
# admin.site.register(Notifications, NotificationsAdmin)
# admin.site.register(LightSensors, LightSensorsAdmin)
# admin.site.register(Devices, DevicesAdmin)
# admin.site.register(EnergySensors, EnergySensorsAdmin)
# admin.site.register(UserSettings, UserSettingsAdmin)
# admin.site.register(Favorites, FavoritesAdmin)
