# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 15:39
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


@allure.feature("TestMimeCase")
class TestMimeCase:

    @allure.story("Mime")
    @allure.description("我的模块退出登录")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-714-2.html", name="测试用例位置")
    @allure.title("我的模块退出登录")
    @allure.step("切换到我的页面")
    @allure.step("进入个人中心页面")
    @allure.step("点击退出登录")
    def test_d4(self,login_activity_class_load,Mime_activity_class_load,function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        Mime_activity_class_load.Mime_btn()
        Mime_activity_class_load.insert_page()
        Mime_activity_class_load.tuichu_btn()
        Mime_activity_class_load.sure_tuichu_btn()
        time.sleep(2)
        message_value = Mime_activity_class_load.get_login_name()
        AssertMethod.assert_equal_screen_shot(function_driver,(message_value,"登录"))


    @allure.story("Mime")
    @allure.description("撤销同意")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-856-2.html", name="测试用例位置")
    @allure.title("执行测试用例用于撤回同意")
    @allure.step("切换到我的页面")
    @allure.step("进入个人信息保护页面")
    @allure.step("点击撤销同意")
    @allure.step("点击确认")
    def test_d5(self,login_activity_class_load,Mime_activity_class_load,function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        time.sleep(2)
        Mime_activity_class_load.Mime_btn()
        Mime_activity_class_load.personal_btn()
        Mime_activity_class_load.reset_agree()
        Mime_activity_class_load.reset_agree_btn()
        time.sleep(2)
        message_value = Mime_activity_class_load.get_login_name()
        AssertMethod.assert_equal_screen_shot(function_driver,(message_value,"登录"))


    @allure.story("Mime")
    @allure.description("检测版本推荐")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-856-2.html", name="测试用例位置")
    @allure.title("执行测试用例用于检测固件升级")
    @allure.step("切换到我的页面")
    @allure.step("进入关于页面")
    @allure.step("点击版本信息")
    def test_d6(self,login_activity_class_load,Mime_activity_class_load,function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        time.sleep(2)
        Mime_activity_class_load.Mime_btn()
        Mime_activity_class_load.about_btn()
        Mime_activity_class_load.version_btn()
        time.sleep(2)
        message_value = Mime_activity_class_load.update_notice()
        AssertMethod.assert_equal_screen_shot(function_driver,(message_value,"应用更新"))



    @allure.story("Mime")
    @allure.description("检测版本推荐")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-856-2.html", name="测试用例位置")
    @allure.title("执行测试用例用于开启设备推送")
    @allure.step("切换到我的页面")
    @allure.step("进入消息设置页面")
    @allure.step("开启设备推送按钮")
    def test_d7(self,login_activity_class_load,Mime_activity_class_load,function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        Mime_activity_class_load.Mime_btn()
        Mime_activity_class_load.find_and_click_element('information_set')
        Mime_activity_class_load.get_devicesinformation()
        time.sleep(2)
        message_value = Mime_activity_class_load.devices_door()
        AssertMethod.assert_true_screen_shot(function_driver,message_value)


    @allure.story("Mime")
    @allure.description("切换语言为英语")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-896-2.html", name="测试用例位置")
    @allure.title("执行测试用例用于切换英语")
    @allure.step("切换到我的页面")
    @allure.step("进入选择语言页面")
    @allure.step("设置为英语")
    # @pytest.mark.skipif(1==1,reason='跳过切换为英语的用例，对后续测试用例有影响')
    def test_d8(self,login_activity_class_load,Mime_activity_class_load,function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        Mime_activity_class_load.Mime_btn()
        Mime_activity_class_load.language_select()
        Mime_activity_class_load.language_english()
        time.sleep(2)
        message_value = Mime_activity_class_load.sure_english()
        AssertMethod.assert_equal_screen_shot(function_driver,(message_value,'Select language'))



    @allure.story("Mime")
    @allure.description("修改昵称为1个字符")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-1335-1.html", name="测试用例位置")
    @allure.title("执行测试用例用于修改用户昵称")
    @allure.step("切换到我的页面")
    @allure.step("进入昵称")
    @allure.step("清除输入框内容，输入1")
    @allure.step("点击确认按钮")
    def test_d9(self,login_activity_class_load,Mime_activity_class_load,function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        Mime_activity_class_load.Mime_btn()
        Mime_activity_class_load.insert_page()
        Mime_activity_class_load.insert_page()
        Mime_activity_class_load.dingwei_wenbenkuang()
        Mime_activity_class_load.input_kuang('1')
        Mime_activity_class_load.sure_tuichu_btn()
        time.sleep(2)
        message_value = Mime_activity_class_load.get_toash1()
        AssertMethod.assert_equal_screen_shot(function_driver,(message_value,'昵称需在2-30个字符内'))

    @allure.story("Mime")
    @allure.description("修改昵称为30个字符")
    @allure.testcase("https://zentao.ugreeniot.com/testcase-view-1335-1.html", name="测试用例位置")
    @allure.title("执行测试用例用于修改用户昵称")
    @allure.step("切换到我的页面")
    @allure.step("进入昵称")
    @allure.step("清除输入框内容，输入30个1")
    @allure.step("点击确认按钮")
    def test_d10(self, login_activity_class_load, Mime_activity_class_load, function_driver):
        logging.info("用例编号编码：{}".format(inspect.stack()[0][3]))
        Mime_activity_class_load.Mime_btn()
        Mime_activity_class_load.insert_page()
        Mime_activity_class_load.insert_page()
        Mime_activity_class_load.dingwei_wenbenkuang()
        Mime_activity_class_load.input_kuang('111111111111111111111111111111')
        Mime_activity_class_load.sure_tuichu_btn()
        time.sleep(2)
        message_value = Mime_activity_class_load.personal_name()
        AssertMethod.assert_equal_screen_shot(function_driver, (message_value, '111111111111111111111111111111'))



if __name__ == "__main__":
    pytest.main(["--alluredir=Report/android", "--clean-alluredir", "test_loginActivityCase.py::TestLoginPageCase"])
    # pytest.main(["test_loginActivityCase.py"])