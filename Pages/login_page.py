#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2023/9/18
# @Author  : 
# @File    : login_page 针对这个页面写一些方法
from Locators.login_page_locator.login_page_locator import LoginLocator as loc
from Common.plugs.basepage import BasePage


class LoginPage(BasePage):

    # 登录
    def login(self, username, password):
        doc = '登录页面_登录功能'
        self.find_element('username',loc.username_loc).send_keys(username)
        self.find_element('password',loc.password_loc).send_keys(password)
        self.click_element('submit', loc.login_btn_loc)

    # 获取错误提示
    def get_login_errMsg(self):
        doc = '登录页面_登录功能错误信息_获取错误信息'
        # self.wait_eleVisible(loc.error_msg_loc)
        return self.find_element(doc, loc.error_msg_loc).text

