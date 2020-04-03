"""
# https://pymotw.com/3/configparser/
"""
import configparser
import os


def get_constant_value(config_file='config.ini', constant_section='DEFAULT', constant_variable='NONE'):
    config = configparser.ConfigParser()
    # Reading single configuration file
    config.read(config_file)
    constant_value = config.get(constant_section, constant_variable)
    return constant_value


def read_multiple_config_file(config_files_list=None, constant_section='DEFAULT', constant_variable='NONE'):
    config = configparser.ConfigParser()
    # Reading multiple configuration files to get a particular value from a section
    config.read(config_files_list)
    constant_value = config.get(constant_section, constant_variable)
    return constant_value


val_1 = get_constant_value(config_file='CONFIG_2.ini', constant_section='PART_A', constant_variable='STRING1')
print(val_1)
configs = [file for file in os.listdir('.') if file.endswith('.INI') or file.endswith('.ini')]
val_2 = read_multiple_config_file(config_files_list=configs, constant_section='PART_A', constant_variable='STRING3')
print(val_2)
