# -*- coding: utf-8 -*-
# @Time    : 2024/8/22 14:33
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest
from ActivityObject.Home_activity.HomeActivity import HomeActivity



@pytest.fixture(scope="function")
def Home_activity_class_load(function_driver):
    Home_activity = HomeActivity(function_driver)
    yield Home_activity