#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2023/9/18
# @Author  : 
# @File    : get_config 读取/修改配置文件的方法
import configparser
import logging
# import os
import sys
from public_obj import conf_dir
# BASE_DIR = os.path.dirname(os.path.dirname(os.getcwd()))
# print(BASE_DIR)
# if sys.platform == 'win32':
#     conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
# else:
#     conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')

# print(conf_dir)
class Config(object):

    def __init__(self, path):
        self.path = path
        self.cf = configparser.ConfigParser()
        self.cf.read(self.path, encoding='utf-8')

    def get(self, field, key):
        """
        对ConfigParser().get方法封装一层异常处理，读取配置文件指定部分field的信息
        :param field:
        :param key:
        :return:
        """
        try:
            result = self.cf.get(field, key)
        except Exception as e:
            logging.info(f'没有读取到配置文件的内容{e}')
            result = ''
        return result

    def set(self, field, key, value):
        """
        对ConfigParser().set方法封装一层异常处理，对配置文件中指定部分下的选项的值进行修改设置
        :param field:
        :param key:
        :param value:
        :return:
        """
        try:
            self.cf.set(field, key, value)
            self.cf.write(open(self.cf, 'w'))
        except Exception as e:
            logging.error(f'Config.set()方法执行报错{e}')
            return False
        return True


def r_config(config_file_path, field, key):
    """
    对ConfigParser().read()方法封装一层异常处理，读取特定配置文件的指定部分的内容
    :param config_file_path:
    :param field:
    :param key:
    :return:
    """
    rf = configparser.ConfigParser()
    try:
        rf.read(config_file_path, encoding='utf-8')
        if sys.platform == 'win32':
            result = rf.get(field, key).replace('/', '\\')
        else:
            result = rf.get(field, key)
    except Exception as e:
        logging.error(f'读取配置文件出错: {e}')
        sys.exit(1)
    return result


def w_config(config_file_path, field, key, value):
    """
    对ConfigParser的写入配置文件的流程封装一层异常处理，支持读取配置文件-修改读取的特定部分-写回配置文件
    :param config_file_path:
    :param field:
    :param key:
    :param value:
    :return:
    """
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file_path)
        cf.set(field, key, value)
        cf.write(open(config_file_path, 'w'))
    except Exception as e:
        logging.error(f'修改配置文件失败{e}')
        sys.exit(1)
    return True


if __name__ == '__main__':
    print(conf_dir)
    result = r_config(conf_dir, 'log', 'log_path')
    print(result)
