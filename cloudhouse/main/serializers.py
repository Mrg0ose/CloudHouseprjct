from rest_framework import serializers
from .models import *


class VoiceSensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceSensors
        fields = '__all__'


class EnergySensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergySensors
        fields = '__all__'


class TemperatureSensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureSensors
        fields = '__all__'


class LightSensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightSensors
        fields = '__all__'


class ReportSensorsParamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSensorsParams
        fields = '__all__'


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'


class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = '__all__'


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = '__all__'


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
