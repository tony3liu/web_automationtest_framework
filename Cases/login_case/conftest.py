#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2023/9/18
# @Author  : 
# @File    : conftest
import time

import pytest
from Common.plugs.get_config import r_config
from Common.plugs.get_log import Log
from Pages.login_page import LoginPage
from public_obj import conf_dir, driver
from TestData.GobalDatas import gobal_datas as GD

log_dir = r_config(conf_dir, 'log', 'log_path')
logger = Log(conf_dir)


@pytest.fixture(scope='class')
def start_module():
    """
    每个模块单独打开一次浏览器，此时 driver.quit() 需要单独加上
    :return:
    """
    logger.info("==========开始执行测试用例集===========")
    driver.get(GD.web_login_url)
    lg = LoginPage()

    yield (driver, lg) # 执行用例后
    logger.info("==========结束执行测试用例集===========")
    driver.quit()


@pytest.fixture(scope='class')
def start_session():
    """
    所有模块只打开一次浏览器
    :return:
    """
    logger.info("==========开始执行测试用例集===========")
    driver.get(GD.web_login_url)
    lg = LoginPage()

    yield(driver,lg)  # 执行用例后
    logger.info("==========结束执行测试用例集===========")


@pytest.fixture()
def refresh_page():
    yield
    driver.refresh()
    time.sleep(3)
