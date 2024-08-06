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
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-277-1.html", name="测试用例位置")
    @allure.title("执行测试用例用于登录模块")
    @allure.step("打开绿联app")
    @allure.step("输入手机号码")
    @allure.step("输入密码")
    @allure.step("勾选已读，点击登陆按钮")
    def test_d1(self, login_activity_class_load, function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        login_activity_class_load.input_phone("15992213991")
        login_activity_class_load.input_passage("abcd123")
        login_activity_class_load.click_chenkbox_btn()
        login_activity_class_load.click_login_btn()
        AssertMethod.assert_equal_screen_shot(function_driver, ('Success!', "密码错误"))



if __name__ == "__main__":
    pytest.main(["--alluredir=Report/android", "--clean-alluredir", "test_loginActivityCase.py::TestLoginPageCase"])
    # pytest.main(["test_loginActivityCase.py"])
