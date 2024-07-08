from aifc import Error

import mysql.connector


class MysqlClient:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        # Подключение к серверу
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      user=self.user,
                                                      password=self.password,
                                                      database=self.database)
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Ошибка подключения к серверу MySQL: {e}")
            exit()

    def insert_report_sensors(self, sensor_data_temperature_report, sensor_data_energy_report,
                              sensor_data_voice_report):
        query_energy_report = "INSERT INTO report_sensors_params (energy_id, user_id,float_param,int_param,date_param,time_param,type_sensor) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        query_temperature_report = "INSERT INTO report_sensors_params (temp_id, user_id,int_param,date_param,time_param,type_sensor) VALUES (%s, %s, %s, %s, %s, %s)"
        query_voice_report = "INSERT INTO report_sensors_params (voice_id, user_id,int_param,date_param,time_param,type_sensor) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.executemany(query_temperature_report, sensor_data_temperature_report)
        self.cursor.executemany(query_energy_report, sensor_data_energy_report)
        self.cursor.executemany(query_voice_report, sensor_data_voice_report)
        self.connection.commit()

    def last_param_update_sensors(self, sensor_data_energy_update, sensor_data_voice_update,
                                  sensor_data_temperature_update):
        query_temperature_update = "UPDATE temperature_sensors SET temperature_result = %s, lastpar_date = %s, lastpar_time = %s where sensor_id = %s"
        query_voice_update = "UPDATE voice_sensors SET voice_result = %s, lastpar_date = %s, lastpar_time = %s where sensor_id = %s"
        query_energy_update = "UPDATE energy_sensors SET sensor_result_energy = %s,sensor_result_voltage = %s, lastpar_date = %s, lastpar_time = %s where sensor_id = %s"
        self.cursor.executemany(query_temperature_update, sensor_data_temperature_update)
        self.cursor.executemany(query_voice_update, sensor_data_voice_update)
        self.cursor.executemany(query_energy_update, sensor_data_energy_update)
        self.connection.commit()
