#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2023/9/18
# @Author  : 
# @File    : basepage 基础的页面方法
import datetime
import os
import sys
import time
from selenium.webdriver.support import expected_conditions as EC, wait
from public_obj import conf_dir, driver
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log

# NOTICE: 这是我这个的框架设计缺陷，后面需要改进，把一些公用的对象放在一个py模块里,现在这么实现是为了防止循环调用
# NOTICE: 后面写公用模块的时候，就不会使用r_config方法，这样就不会陷入循环调用
# BASE_DIR = os.path.dirname(os.path.dirname(os.getcwd()))
# if sys.platform == 'win32':
#     conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
# else:
#     conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
# driver_path = r_config(conf_dir, 'chrome_driver', 'chrome_driver')
# driver = webdriver.Chrome(executable_path=driver_path)

img_path = r_config(conf_dir, 'image', 'img_path')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)


# 封装基本函数 - 执行日志、 异常处理、 截图
class BasePage:
    def __init__(self):
        self.driver = driver

    def save_screenshot(self, pic_name=None):
        img_name = os.path.join(img_path, f'{pic_name}{time.time()}')
        try:
            self.driver.get_screenshot_as_file(img_name)
        except Exception as e:
            logger.info(f'截图失败：{e}')

    def wait_eleVisible(self, ele_name, locator):
        """
        等待元素可见的方法封装
        :param ele_name:
        :param locator:元组(BY.XPATH,"xxx")
        :return:
        """
        try:
            start = datetime.datetime.now()
            wait.WebDriverWait(self.driver, timeout=20) \
                .until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info(f'{ele_name}等待页面元素可见，共耗时{wait_time}s')
        except Exception as e:
            logger.error(f'{ele_name}等待页面元素不可见，20s超时')
            self.save_screenshot(pic_name=ele_name)

    def find_element(self, ele_name, locator):
        """
        定位元素方法封装
        :param ele_name:
        :param locator:元组(BY.XPATH,"xxx")
        :return:
        """
        self.wait_eleVisible(ele_name=ele_name, locator=locator)
        return self.driver.find_element(locator)

    def click_element(self, ele_name, locator):
        """
        判断元素可点击了，才去点击
        NOTICE：这里面有个重复判断的过程，因为定位元素的时候也去判断了一遍元素是否出现，后续可以改进
        :param ele_name:
        :param locator:元组(BY.XPATH,"xxx")
        :return:
        """
        try:
            start = datetime.datetime.now()
            wait.WebDriverWait(self.driver, timeout=30).until(EC.element_to_be_clickable(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info(f'{ele_name}等待页面元素:{locator}:可点击，共耗时{wait_time}s')
        except Exception as e:
            logger.info(f'{ele_name}元素不可点击{e}')
            self.save_screenshot(pic_name=f'{ele_name}元素不可点击')
            sys.exit(1)
        self.find_element(ele_name=ele_name, locator=locator).click()

    # alter 处理
    def alter_action(self):
        pass

    # iframe 切换
    def switch_iframe(self):
        pass

    # windows 切换
    def switch_window(self):
        pass

    # 上传操作
    def upload_file(self):
        pass



