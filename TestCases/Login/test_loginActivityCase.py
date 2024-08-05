# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/16 21:11
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : run.py
# @Software: PyCharm
import pytest
import allure
import inspect
import logging
from Base.assertMethod import AssertMethod


@allure.feature("TestLoginPageCase")
class TestLoginPageCase:

    @allure.story("Login")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_d1(self, login_activity_class_load, function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        login_activity_class_load.input_phone("15992213991")
        login_activity_class_load.input_passage("abcd1234")
        login_activity_class_load.click_chenkbox_btn()
        login_activity_class_load.click_login_btn()
        # AssertMethod.assert_equal_screen_shot(function_driver, (message_value, "用户不存在"))

    @allure.story("Login")
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.link("https://www.baidu.com", name="连接跳转百度")
    @allure.testcase("https://www.sina.com", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    def test_d2(self, login_activity_class_load, function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        login_activity_class_load.input_phone("18383398524")
        login_activity_class_load.input_code("123456")
        login_activity_class_load.click_login_btn()
        message_value = login_activity_class_load.get_message_value()
        AssertMethod.assert_equal_screen_shot(function_driver, (message_value, "用户存在"))


if __name__ == "__main__":
    pytest.main(["test_loginActivityCase.py"])
