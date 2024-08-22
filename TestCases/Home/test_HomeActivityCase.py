# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/22 15:39
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : test_MimeActivityCase.py
# @Software: PyCharm
import time

import pytest
import allure
import inspect
import logging
from Base.assertMethod import AssertMethod


@allure.feature("TestHomeCase")
class TestHomeCase:

    @allure.story("Home")
    @allure.description("我的模块退出登录")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-714-2.html", name="测试用例位置")
    @allure.title("我的模块退出登录")
    @allure.step("切换到我的页面")
    @allure.step("进入个人中心页面")
    @allure.step("点击退出登录")
    def test_d11(self,login_activity_class_load,Home_activity_class_load,function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        Home_activity_class_load.person_logo()
        time.sleep(2)
        message_value = Home_activity_class_load.language_select()
        AssertMethod.assert_equal_screen_shot(function_driver,(message_value,"语言设置"))