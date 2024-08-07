# -*- coding: utf-8 -*-
# @Time    : 2024/7/27 9:15
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
import logging
from appium import webdriver
from Common.publicMethod import PubMethod

appium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "appium_config.yaml")
appium_config = PubMethod.read_yaml(appium_config_path)["appium_config"]



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


@pytest.fixture(scope="function")
def function_driver(request):
    desired_caps = {
        'platformName': appium_config['platformName'],
        'deviceName': appium_config['deviceName'],
        'platformVersion': appium_config['platformVersion'],
        'appPackage': appium_config['appPackage'],
        'appActivity': appium_config['appActivity'],
        'unicodeKeyboard': appium_config['unicodeKeyboard'],
        'resetKeyboard': appium_config['resetKeyboard'],
        # 'newCommandTimeout': 60  # 添加超时设置
    }
    try:
        logging.info(f"Connecting to Appium server at {appium_config['remote_URL']} with capabilities {desired_caps}")
        driver = webdriver.Remote(
           appium_config["remote_URL"],desired_capabilities=desired_caps
        )
    except Exception as e:
        logging.error(f"Failed to create WebDriver instance: {e}")
        raise
    yield driver
    driver.quit()
    # driver = webdriver.Remote(command_executor=appium_config["remote_URL"], desired_capabilities=desired_caps)
    # yield driver
    # logging.info("driver.quit:清理driver进程！！！")
    # driver.quit()


if __name__ == '__main__':
    print(appium_config["remote_URL"])

