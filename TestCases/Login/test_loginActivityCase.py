# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 10:33
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : test_loginActivityCase.py
# @Software: PyCharm
import time

import pytest
import allure
import inspect
import logging
from Base.assertMethod import AssertMethod


@allure.feature("TestLoginPageCase")
class TestLoginPageCase:

    @allure.story("Login")
    @allure.description("测试登录")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-277-1.html", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    @allure.step("打开绿联app")
    @allure.step("输入手机号码")
    @allure.step("输入密码")
    @allure.step("连续两次点击登陆按钮")
    def test_d1(self,login_activity_class_load):
        # 登录已经在 fixture 中完成
        message_value = login_activity_class_load.add_devices()
        # assert message_value == "添加设备"
        driver = login_activity_class_load.driver
        AssertMethod.assert_equal_screen_shot(driver, (message_value, "添加设备"))



    @allure.story("Login")
    @allure.description("测试登录密码出错")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-1334-1.html", name="测试用例位置")
    @allure.title("执行测试用例用于登录密码错误模块")
    @allure.step("打开绿联app")
    @allure.step("输入手机号码")
    @allure.step("输入错误密码")
    @allure.step("勾选已读，点击登陆按钮")
    def test_d2(self,login_activity_class_loading,function_driver):
        login_activity_class_loading.login_btn_successs()
        login_activity_class_loading.input_phone("15992213991")
        login_activity_class_loading.input_passage("abcd12345")
        login_activity_class_loading.click_login_btn()
        login_activity_class_loading.click_chenkbox_btn()  # 勾选复选框
        login_activity_class_loading.click_login_btn()  # 点击登录按钮
        # 获取toash信息
        message_value = login_activity_class_loading.get_passage_error_toash()
        AssertMethod.assert_equal_screen_shot(function_driver, (message_value, "密码错误"))



    @allure.story("Login")
    @allure.description("测试登录密码出错")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-1334-1.html", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    @allure.step("打开绿联app")
    @allure.step("输入手机号码")
    @allure.step("输入正确密码")
    @allure.step("勾选已读，点击登陆按钮")
    def test_d3(self,login_activity_class_loading,function_driver):
        login_activity_class_loading.login_btn_successs()
        login_activity_class_loading.input_phone("15992213991")
        login_activity_class_loading.input_passage("abcd1234")
        login_activity_class_loading.check_btn()  # 勾选复选框
        time.sleep(2)
        login_activity_class_loading.click_login_btn()  # 点击登录按钮
        # 获取登录后信息
        message_value = login_activity_class_loading.add_devices()
        AssertMethod.assert_equal_screen_shot(function_driver, (message_value, "添加设备"))




if __name__ == "__main__":
    pytest.main(["--alluredir=Report/android", "--clean-alluredir", "test_loginActivityCase.py::TestLoginPageCase"])
    # pytest.main(["test_loginActivityCase.py"])
