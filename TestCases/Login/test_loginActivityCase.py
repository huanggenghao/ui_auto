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
    @allure.severity("normal")
    @allure.description("测试登录")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-277-1.html", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    @allure.step("打开绿联app")
    @allure.step("输入手机号码")
    @allure.step("输入密码")
    @allure.step("勾选已读，点击登陆按钮")
    def test_d1(self, login_activity_class_load, function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        login_activity_class_load.login_btn_successs()
        login_activity_class_load.input_phone("15992213991")
        login_activity_class_load.input_passage("abcd1234")
        login_activity_class_load.click_login_btn()
        login_activity_class_load.click_chenkbox_btn()
        login_activity_class_load.click_login_btn()
        time.sleep(2)
        message_value = login_activity_class_load.add_devices()
        AssertMethod.assert_equal_screen_shot(function_driver,(message_value,"添加设备"))



if __name__ == "__main__":
    pytest.main(["--alluredir=Report/android", "--clean-alluredir", "test_loginActivityCase.py::TestLoginPageCase"])
    # pytest.main(["test_loginActivityCase.py"])
