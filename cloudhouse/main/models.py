# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.urls import reverse


class Addresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    id_client = models.ForeignKey('Clients', models.DO_NOTHING, db_column='id_client', blank=True, null=True)
    code_contract = models.ForeignKey('Contracts', models.CASCADE, db_column='code_contract', blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Аккаунт', db_column='user_id')
    name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    patronymic = models.CharField(max_length=45, blank=True, null=True)
    mobile = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=70, blank=True, null=True)
    uncpass = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        managed = False
        db_table = 'clients'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиент'


class Contracts(models.Model):
    code_contract = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING, blank=True, null=True)
    contract_start = models.DateField(blank=True, null=True)
    contract_payment = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    archive = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contracts'
        verbose_name = 'Договор'
        verbose_name_plural = 'Договор'

    def __str__(self):
        return str(self.code_contract)


class Devices(models.Model):
    device_id = models.AutoField(primary_key=True)
    contract_code = models.ForeignKey(Contracts, models.CASCADE, db_column='contract_code', blank=True, null=True)
    device_name = models.CharField(max_length=45, blank=True, null=True)
    device_description = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройство'

    def __str__(self):
        return self.device_name


class EnergySensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Devices, models.CASCADE, blank=True, null=True)
    sensor_name = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    lastpar_date = models.DateField(blank=True, null=True)
    lastpar_time = models.TimeField(blank=True, null=True)
    sensor_result_energy = models.FloatField(blank=True, null=True)
    sensor_result_voltage = models.IntegerField(blank=True, null=True)
    sensor_type = models.CharField(max_length=50, blank=True, null=True)
    max_energy = models.FloatField(blank=True, null=True)
    min_energy = models.FloatField(blank=True, null=True)
    max_voltage = models.IntegerField(blank=True, null=True)
    min_voltage = models.IntegerField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'energy_sensors'
        verbose_name = 'Датчик электросбережения'
        verbose_name_plural = 'Датчик электросбережения'

    def __str__(self):
        return self.sensor_name


class Favorites(models.Model):
    favorit_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Аккаунт', db_column='user_id')
    energy_sensor = models.ForeignKey(EnergySensors, models.DO_NOTHING, blank=True, null=True)
    light_sensor = models.ForeignKey('LightSensors', models.DO_NOTHING, blank=True, null=True)
    voice_sensor = models.ForeignKey('VoiceSensors', models.DO_NOTHING, blank=True, null=True)
    temp_sensor = models.ForeignKey('TemperatureSensors', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.user_id.username

    class Meta:
        managed = False
        db_table = 'favorites'
        verbose_name = 'Избранные'
        verbose_name_plural = 'Избранные'


class LightSensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Devices, models.CASCADE, blank=True, null=True)
    sensor_name = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    lastpar_date = models.DateField(blank=True, null=True)
    lastpar_time = models.TimeField(blank=True, null=True)
    light_result = models.IntegerField(blank=True, null=True)
    sensor_type = models.CharField(max_length=50, blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.sensor_name

    class Meta:
        managed = False
        db_table = 'light_sensors'
        verbose_name = 'Датчик света'
        verbose_name_plural = 'Датчик света'


class Notifications(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Аккаунт', db_column='user_id')
    notification_type = models.CharField(max_length=45, blank=True, null=True)
    notification_description = models.TextField(blank=True, null=True)
    notification_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'
        verbose_name = 'Уведомления'
        verbose_name_plural = 'Уведомления'


class ReportSensorsParams(models.Model):
    report_sensors_params_id = models.AutoField(primary_key=True)
    energy = models.ForeignKey(EnergySensors, models.CASCADE, blank=True, null=True)
    temp = models.ForeignKey('TemperatureSensors', models.CASCADE, blank=True, null=True)
    voice = models.ForeignKey('VoiceSensors', models.CASCADE, blank=True, null=True)
    light = models.ForeignKey(LightSensors, models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Аккаунт', db_column='user_id')
    float_param = models.FloatField(blank=True, null=True)
    bool_param = models.IntegerField(blank=True, null=True)
    int_param = models.IntegerField(blank=True, null=True)
    date_param = models.DateField(blank=True, null=True)
    time_param = models.TimeField(blank=True, null=True)
    type_sensor = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user_id

    class Meta:
        managed = False
        db_table = 'report_sensors_params'
        verbose_name = 'Отчётные данные датчиков'
        verbose_name_plural = 'Отчётные данные датчиков'


class TemperatureSensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Devices, models.CASCADE, blank=True, null=True)
    sensor_name = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    lastpar_date = models.DateField(blank=True, null=True)
    lastpar_time = models.TimeField(blank=True, null=True)
    temperature_result = models.IntegerField(blank=True, null=True)
    sensor_type = models.CharField(max_length=50, blank=True, null=True)
    max_temperature = models.IntegerField(blank=True, null=True)
    min_temperature = models.IntegerField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.sensor_name

    class Meta:
        managed = False
        db_table = 'temperature_sensors'
        verbose_name = 'Датчик температуры'
        verbose_name_plural = 'Датчик температуры'


class UserSettings(models.Model):
    id_setting = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Аккаунт', db_column='user_id')
    device_start_stop = models.IntegerField(blank=True, null=True)
    email_message = models.IntegerField(blank=True, null=True)
    time_sensors = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} настройки'

    def get_absolute_url(self):
        return reverse('user-settings-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'user_settings_{self.user.pk}')

    class Meta:
        managed = False
        db_table = 'user_settings'
        verbose_name = 'Настройки аккаунта'
        verbose_name_plural = 'Настройки аккаунта'


class VoiceSensors(models.Model):
    sensor_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Devices, models.CASCADE, blank=True, null=True)
    sensor_name = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    lastpar_date = models.DateField(blank=True, null=True)
    lastpar_time = models.TimeField(blank=True, null=True)
    voice_result = models.IntegerField(blank=True, null=True)
    sensor_type = models.CharField(max_length=50, blank=True, null=True)
    voice_min = models.IntegerField(blank=True, null=True)
    voice_max = models.IntegerField(blank=True, null=True)
    favorite = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.sensor_name

    class Meta:
        managed = False
        db_table = 'voice_sensors'
        verbose_name = 'Датчик звука'
        verbose_name_plural = 'Датчик звука'
