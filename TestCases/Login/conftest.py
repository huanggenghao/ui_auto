# -*- coding: utf-8 -*-
# @Time    : 2024/8/14 11:19
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest
from ActivityObject.Login_activity.loginActivity import LoginActivity



@pytest.fixture(scope="function")
def login_activity_class_loading(function_driver):
    Login_activity = LoginActivity(function_driver)
    yield Login_activity
