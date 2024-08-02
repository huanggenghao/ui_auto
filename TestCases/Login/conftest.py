# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 22:53
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest
from ActivityObject.Login_activity.loginActivity import LoginActivity


@pytest.fixture(scope="function")
def login_activity_class_load(function_driver):
    login_activity = LoginActivity(function_driver)
    yield login_activity


