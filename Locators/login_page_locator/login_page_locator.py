#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2023/9/18
# @Author  : 
# @File    : login_page_locator
from selenium.webdriver.common.by import By


# example:
class LoginLocator:
    username_loc = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input')
    password_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
    login_btn_loc = (By.XPATH, '//*[@type="button"]')
    error_msg_loc = (By.CLASS_NAME, 'el-message__content')