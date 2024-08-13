# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/6 11:23
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : loginActivity.py
# @Software: PyCharm
from Base.base import Base
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

    def login_btn_successs(self):
        elem = self.elem_locator.get_locator("login_btn_successs")
        super().click_btn(elem)

    def add_devices(self):
        elem = self.elem_locator.get_locator("add_devices")
        return super().get_text(elem)



