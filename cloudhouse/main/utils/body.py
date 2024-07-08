import datetime
import time
from aifc import Error

from ..models import UserSettings



from ..utils import class_sensor
from ..utils import mysqlconnect


class CentralUnit:
    def __init__(self):
        self.mysql_client = mysqlconnect.MysqlClient(host="localhost",
                                        user="root",
                                        password="Vlad19042001",
                                        database="cloudhousedb")

        self.temp_sensor1 = class_sensor.TemperatureSensors(sensor_id="1", user_id="2", data_type='Температура')

        self.voice_sensor1 = class_sensor.VoiceSensors(sensor_id="1", user_id="2", data_type='Звук')

        self.energy_sensor1 = class_sensor.EnergySensors(sensor_id="1", user_id="2", data_type='Электричество')

        self.temp_sensor2 = class_sensor.TemperatureSensors(sensor_id="2", user_id="2", data_type='Температура')

        self.voice_sensor2 = class_sensor.VoiceSensors(sensor_id="3", user_id="2", data_type='Звук')

        self.energy_sensor2 = class_sensor.EnergySensors(sensor_id="2", user_id="2", data_type='Электричество')
        # тест клиент ниже

        self.temp_sensor3 = class_sensor.TemperatureSensors(sensor_id="21", user_id="8", data_type='Температура')

        self.voice_sensor3 = class_sensor.VoiceSensors(sensor_id="2", user_id="8", data_type='Звук')

        self.energy_sensor3 = class_sensor.EnergySensors(sensor_id="3", user_id="8", data_type='Электричество')
        # тест клиент ниже
        self.temp_sensor4 = class_sensor.TemperatureSensors(sensor_id="22", user_id="9", data_type='Температура')

        self.voice_sensor4 = class_sensor.VoiceSensors(sensor_id="4", user_id="9", data_type='Звук')

        self.energy_sensor4 = class_sensor.EnergySensors(sensor_id="4", user_id="9", data_type='Электричество')
        # тест клиент ниже
        self.temp_sensor5 = class_sensor.TemperatureSensors(sensor_id="23", user_id="10", data_type='Температура')

        self.voice_sensor5 = class_sensor.VoiceSensors(sensor_id="5", user_id="10", data_type='Звук')

        self.energy_sensor5 = class_sensor.EnergySensors(sensor_id="5", user_id="10", data_type='Электричество')

        self.sensors_temperature = [self.temp_sensor1, self.temp_sensor2, self.temp_sensor3, self.temp_sensor4, self.temp_sensor5]
        self.sensors_energy = [self.energy_sensor1, self.energy_sensor2, self.energy_sensor3, self.energy_sensor4, self.energy_sensor5]
        self.sensors_voice = [self.voice_sensor1, self.voice_sensor2, self.voice_sensor3, self.voice_sensor4, self.voice_sensor5]

    def read_sensor_temperature_values(self):
        for sensor in self.sensors_temperature:
            sensor.read_value()

    def read_sensor_energy_values(self):
        for sensor in self.sensors_energy:
            sensor.read_value()

    def read_sensor_voice_values(self):
        for sensor in self.sensors_voice:
            sensor.read_value()


    def send_sensor_data_to_mysql(self):
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.strftime("%Y-%m-%d")
            self.read_sensor_temperature_values()
            self.read_sensor_energy_values()
            self.read_sensor_voice_values()

            sensor_data_temperature_report = [
                (sensor.sensor_id, sensor.user_id, sensor.value, current_date, current_time, sensor.data_type) for sensor in self.sensors_temperature]
            sensor_data_energy_report = [(sensor.sensor_id, sensor.user_id, sensor.value_energy, sensor.value_voltage, current_date, current_time, sensor.data_type) for sensor in self.sensors_energy]
            sensor_data_voice_report = [
                (sensor.sensor_id, sensor.user_id, sensor.value, current_date, current_time, sensor.data_type) for sensor in self.sensors_voice]

            sensor_data_temperature_update = [(sensor.value, current_date, current_time, sensor.sensor_id) for
                                              sensor in self.sensors_temperature]
            sensor_data_voice_update = [(sensor.value, current_date, current_time, sensor.sensor_id) for
                                        sensor in
                                        self.sensors_voice]
            sensor_data_energy_update = [
                (sensor.value_energy, sensor.value_voltage, current_date, current_time, sensor.sensor_id) for
                sensor in self.sensors_energy]


            try:
                # self.mysql_client.insert_report_sensors(sensor_data_temperature_report, sensor_data_energy_report,
                #                                         sensor_data_voice_report)
                self.mysql_client.last_param_update_sensors(sensor_data_energy_update, sensor_data_voice_update,
                                                            sensor_data_temperature_update)
            except Error as e:
                print(f"Error inserting data into database: {e}")


