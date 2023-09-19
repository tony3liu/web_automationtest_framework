#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2023/9/19
# @Author  : 
# @File    : public_obj
import os
import sys
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
cf = ConfigParser()
BASE_DIR = os.path.dirname(__file__)
# print(BASE_DIR)
if sys.platform == 'win32':
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
cf.read(conf_dir, encoding='utf-8')
print(conf_dir)
if sys.platform == 'win32':
    driver_path = cf.get('chrome_driver', 'chrome_driver').replace('/', '\\')
    img_path = cf.get('image', 'img_path').replace('/', '\\')
    log_dir = cf.get("log", "log_path").replace('/', '\\')
else:
    driver_path = cf.get('chrome_driver', 'chrome_driver')
    img_path = cf.get('image', 'img_path')
    log_dir = cf.get("log", "log_path")
# print(driver_path) 下面会报错，因为现在临时填的driver路径，并没有driver
service = ChromeService(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
