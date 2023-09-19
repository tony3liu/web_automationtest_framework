#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2023/9/18
# @Author  : 
# @File    : login_case
import sys

import pytest

from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log
from TestData.login_data import logindata as LD
from public_obj import conf_dir

log_dir = r_config(conf_dir, 'log', 'log_path')
logger = Log(conf_dir)


@pytest.mark.usefixtures('start_module')
@pytest.mark.usefixtures('start_session')
@pytest.mark.usefixtures('refresh_page')
class TestLogin:

    # 异常用例
    @pytest.mark.parametrize('data', LD.error_usernameFormat_data)
    def test_login_username(self, data, start_session, my_function=None):
        logger.info(f"执行 {my_function.__name__} 测试用例")
        logger.info(" 异常测试用例：{0} ".format(data['name']))
        # 后面写断言逻辑
        try:
            assert start_session[1].get_login_errMsg() == data['errorMsg']
            start_session[1].save_screenshot(f"{data['name']}-异常截图")
        except Exception as e:
            logger.error(e)
            raise

    @pytest.mark.smoke
    @pytest.mark.lucas
    # 加两个标记smoke和lucas，到时候pytest -k 标记 去执行特定标记用例
    def test_login_sucess(self, start_session, my_function=None):
        logger.info(f"执行 {my_function.__name__} 测试用例")
        logger.info(" 正常登录测试用例 ")
        # 前置  访问登录页面
        # 步骤  输入用户名 密码 点击登录
        # 断言  首页中 能否找到退出 这个元素
        start_session[1].login(LD.success_data['username'], LD.success_data['password'])
        logger.info("期望值：{0}".format(True))
        logger.info("实际值：{0}".format(LD(start_session[0]).isExist_logout_ele()))
        try:
            assert LD(start_session[0]).isExist_logout_ele()
            start_session[1].save_pictuer("{0}-正常截图".format(LD.success_data['name']))
        except:
            start_session[1].save_pictuer("{0}-异常截图".format(LD.success_data['name']))
            raise
