# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 15:31
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest
from ActivityObject.Mime_activity.MimeActivity import MimeActivity



@pytest.fixture(scope="function")
def Mime_activity_class_load(function_driver):
    Mime_activity = MimeActivity(function_driver)
    yield Mime_activity
