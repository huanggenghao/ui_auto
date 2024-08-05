# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 21:11
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : run.py
# @Software: PyCharm
from Base.base import Base
from selenium import webdriver
from ActivityObject.elemParams import LoginActivityElem


# 封装绿联app登录页面操作对象操作方法
class LoginActivity(Base):
    def __init__(self, driver):
        # 初始化页面元素对象，即yaml文件对象
        self.elem_locator = LoginActivityElem()
        # 初始化driver
        super().__init__(driver)

    def input_phone(self, value):
        elem = self.elem_locator.get_locator("phone_number")
        super().send_key(elem, value)

    def input_passage(self, value):
        elem = self.elem_locator.get_locator("phone_passage")
        super().send_key(elem, value)

    def click_chenkbox_btn(self):
        elem = self.elem_locator.get_locator("checkbox_btn")
        super().click_btn(elem)

    def click_login_btn(self):
        elem = self.elem_locator.get_locator("login_btn")
        super().click_btn(elem)


if __name__ == "__main__":
    home_activity = LoginActivity(webdriver.Chrome())
