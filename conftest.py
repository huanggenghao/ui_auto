# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 9:15
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : conftest.py
# @Software: PyCharm
import os
import time

import pytest
import logging

import yaml
from appium import webdriver

from ActivityObject.Login_activity.loginActivity import LoginActivity
from Common.publicMethod import PubMethod

# appium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "appium_config.yaml")
# appium_config = PubMethod.read_yaml(appium_config_path)["appium_config"]



# 定义钩子函数hook进行测试用例name和_nodeid输出
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        logging.info(item.name)
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")
        logging.info(item._nodeid)


# 定义钩子函数hook实现ios和android系统测试切换
def pytest_addoption(parser):
    parser.addoption("--mobile_system", action="store", default="android", help="choose system version, android or ios")


def get_config_path(mobile_system):
    # 根据系统类型返回配置文件路径
    if mobile_system == "android":
        return os.path.join(os.path.dirname(__file__), "Conf", "appium_config.yaml")
    elif mobile_system == "ios":
        return os.path.join(os.path.dirname(__file__), "Conf", "ios_config.yaml")
    else:
        raise ValueError("Unsupported mobile system")


@pytest.fixture(scope="function")
def function_driver(request):
    # 从 pytest 配置中获取 mobile_system 参数
    mobile_system = request.config.getoption("--mobile_system")

    # 获取配置文件路径
    appium_config_path = get_config_path(mobile_system)

    # 读取配置文件
    appium_config = PubMethod.read_yaml(appium_config_path)["appium_config"]

    desired_caps = {
        'platformName': appium_config['platformName'],
        'deviceName': appium_config['deviceName'],
        'platformVersion': appium_config['platformVersion'],
        # 'appPackage': appium_config['appPackage'],
        # 'appActivity': appium_config['appActivity'],
        # 'app': appium_config.get('app', None),  # iOS 特有
        'unicodeKeyboard': appium_config['unicodeKeyboard'],
        'resetKeyboard': appium_config['resetKeyboard'],
        'newCommandTimeout': 300  # 添加超时设置
    }
    # 根据平台类型添加特定的配置
    if mobile_system == "android":
        desired_caps.update({
            'appPackage': appium_config.get('appPackage'),
            'appActivity': appium_config.get('appActivity')
        })
    elif mobile_system == "ios":
        desired_caps.update({
            'app': appium_config.get('app')
        })

    try:
        logging.info(f"Connecting to Appium server at {appium_config['remote_URL']} with capabilities {desired_caps}")
        driver = webdriver.Remote(
           appium_config["remote_URL"],desired_capabilities=desired_caps
        )
    except Exception as e:
        logging.error(f"Failed to create WebDriver instance: {e}")
        raise
    yield driver

    # 测试用例执行完毕后关闭会话
    logging.info("Closing the Appium session")
    driver.quit()


@pytest.fixture(scope="function")
def login_activity_class_load(function_driver):
    login_activity = LoginActivity(function_driver)

    # 执行登录操作
    login_activity.login_btn_successs()
    login_activity.input_phone("15992213991")
    login_activity.input_passage("abcd1234")
    login_activity.click_login_btn()
    login_activity.click_chenkbox_btn()  # 勾选复选框
    login_activity.click_login_btn()     # 点击登录按钮
    time.sleep(2)

    yield login_activity





