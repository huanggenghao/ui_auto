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



# @allure.feature("TestLoginPageCase")
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
    def test_d1(self,login_activity_class_load):
        # 登录已经在 fixture 中完成
        message_value = login_activity_class_load.add_devices()
        # assert message_value == "添加设备"
        driver = login_activity_class_load.driver
        AssertMethod.assert_equal_screen_shot(driver, (message_value, "添加设备"))




if __name__ == "__main__":
    pytest.main(["--alluredir=Report/android", "--clean-alluredir", "test_loginActivityCase.py::TestLoginPageCase"])
    # pytest.main(["test_loginActivityCase.py"])
