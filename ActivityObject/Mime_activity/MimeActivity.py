# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 14:56
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : MimeActivity.py
# @Software: PyCharm
from Base.base import Base
from ActivityObject.elemParams import  MimeActivityElem


# 封装绿联app登录页面操作对象操作方法
class MimeActivity(Base):
    def __init__(self, driver):
        # 初始化页面元素对象，即yaml文件对象
        self.elem_locator = MimeActivityElem()
        # 初始化driver
        super().__init__(driver)

    def Mime_btn(self):
        elem = self.elem_locator.get_locator("mine_btn")
        super().click_btn(elem)

    def insert_page(self):
        elem = self.elem_locator.get_locator("insert_page")
        super().click_btn(elem)

    def tuichu_btn(self):
        elem = self.elem_locator.get_locator("tuichu_btn")
        super().click_btn(elem)

    def sure_tuichu_btn(self):
        elem = self.elem_locator.get_locator("sure_tuichu_btn")
        super().click_btn(elem)


    def get_login_name(self):
        elem = self.elem_locator.get_locator("login_btn")
        return super().get_text(elem)