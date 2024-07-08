import struct
import random
import sys
sys.path.append('utils')



class TemperatureSensors:
    def __init__(self, sensor_id, user_id, data_type):
        self.sensor_id = sensor_id
        self.user_id = user_id
        self.value = False
        self.data_type = data_type

    def read_value(self):
        if self.data_type == 'Температура':
            self.value = random.uniform(5.0, 17.0)

    def get_registers(self):
        # Преобразование числа с плавающей запятой в два регистра
        reg_list = struct.pack('!f', self.value)
        reg_list = [int.from_bytes(reg_list[i:i + 2], byteorder='big') for i in range(0, 4, 2)]

        return reg_list


class EnergySensors:
    def __init__(self, sensor_id, user_id, data_type):
        self.sensor_id = sensor_id
        self.user_id = user_id
        self.value_voltage = False
        self.value_energy = False
        self.data_type = data_type

    def read_value(self):
        if self.data_type == 'Электричество':
            self.value_energy = random.uniform(300, 350)
            self.value_voltage = random.uniform(110, 220)

    def get_registers_voltage(self):
        # Преобразование числа с целочисленным в два регистра
        reg_list2 = struct.pack('!f', self.value_voltage)
        reg_list2 = [int.from_bytes(bytes(reg_list2[i:i + 2]), byteorder='big') for i in range(0, 2, 2)]

        return reg_list2

    def get_registers_energy(self):
        reg_list2 = struct.pack('!f', self.value_energy)
        reg_list2 = [int.from_bytes(bytes(reg_list2[i:i + 2]), byteorder='big') for i in range(0, 2, 2)]

        return reg_list2


class VoiceSensors:
    def __init__(self, sensor_id, user_id, data_type):
        self.sensor_id = sensor_id
        self.user_id = user_id
        self.value = False
        self.data_type = data_type

    def read_value(self):
        if self.data_type == 'Звук':
            self.value = random.uniform(10, 90)

    def get_registers_voltage(self):
        reg_list3 = struct.pack('!f', self.value)
        reg_list3 = [int.from_bytes(bytes(reg_list3[i:i + 2]), byteorder='big') for i in range(0, 2, 2)]

        return reg_list3
