# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 14:56
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : MimeActivity.py
# @Software: PyCharm
import logging

from Base.base import Base
from ActivityObject.elemParams import  MimeActivityElem
from Common.publicMethod import PubMethod


# 封装绿联app登录页面操作对象操作方法
class MimeActivity(Base):
    def __init__(self, driver):
        # 初始化页面元素对象，即yaml文件对象
        self.elem_locator = MimeActivityElem()
        # 初始化driver
        super().__init__(driver)

    def Mime_btn(self):
        elem = self.elem_locator.get_locator("mine_btn")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def insert_page(self):
        elem = self.elem_locator.get_locator("insert_page")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)

    def tuichu_btn(self):
        elem = self.elem_locator.get_locator("tuichu_btn")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)

    def sure_tuichu_btn(self):
        elem = self.elem_locator.get_locator("sure_tuichu_btn")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def get_login_name(self):
        elem = self.elem_locator.get_locator("login_btn")
        if elem:
                return super().get_text(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)

    def personal_btn(self):
        elem = self.elem_locator.get_locator("personal_btn")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)



    def reset_agree(self):
        elem = self.elem_locator.get_locator("reset_agree")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def reset_agree_btn(self):
        elem = self.elem_locator.get_locator("reset_agree_btn")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def version_btn(self):
        elem = self.elem_locator.get_locator("version_btn")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def about_btn(self):
        elem = self.elem_locator.get_locator("about_btn")
        if elem:
                super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def update_notice(self):
        elem = self.elem_locator.get_locator("update_notice")
        if elem:
               return super().get_text(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)



    def get_devicesinformation(self):
        elem = self.elem_locator.get_locator("get_devicesinformation")
        if elem:
               super().click_btn(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def devices_door(self):
        elem = self.elem_locator.get_locator("devices_door")
        if elem:
                return super().get_radio_button_status(elem)
        else:
             logging.error("获取元素定位器失败")
             screenshout_url = PubMethod.screen_picture(self.driver)


    def find_and_click_element(self, elem_name):
        # 获取元素的定位器
        locator = self.elem_locator.get_locator(elem_name)
        if locator:
            try:
                # 查找并点击元素
                element = self.find_element(locator)
                if element:
                    element.click()
                    logging.info("成功点击元素: {}".format(elem_name))
                else:
                    logging.error("元素找不到: {}".format(elem_name))
                    # 直接调用 PubMethod.screen_picture 进行截图
                    screenshot_url = PubMethod.screen_picture(self.driver)
                    logging.info("截图保存路径: {}".format(screenshot_url))
            except Exception as e:
                logging.error("操作元素时发生错误: {}".format(e))
                # 直接调用 PubMethod.screen_picture 进行截图
                screenshot_url = PubMethod.screen_picture(self.driver)
                logging.info("截图保存路径: {}".format(screenshot_url))
        else:
            logging.error("获取元素定位器失败: {}".format(elem_name))
            # 直接调用 PubMethod.screen_picture 进行截图
            screenshot_url = PubMethod.screen_picture(self.driver)
            logging.info("截图保存路径: {}".format(screenshot_url))



