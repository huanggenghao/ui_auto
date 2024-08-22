# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 14:56
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : MimeActivity.py
# @Software: PyCharm
import logging

from selenium.common import NoSuchElementException

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

    def personal_btn(self):
        elem = self.elem_locator.get_locator("personal_btn")
        super().click_btn(elem)




    def reset_agree(self):
        elem = self.elem_locator.get_locator("reset_agree")
        super().click_btn(elem)



    def reset_agree_btn(self):
        elem = self.elem_locator.get_locator("reset_agree_btn")
        super().click_btn(elem)



    def version_btn(self):
        elem = self.elem_locator.get_locator("version_btn")
        super().click_btn(elem)


    def about_btn(self):
        elem = self.elem_locator.get_locator("about_btn")
        super().click_btn(elem)


    def update_notice(self):
        elem = self.elem_locator.get_locator("update_notice")
        return super().get_text(elem)



    def get_devicesinformation(self):
        elem = self.elem_locator.get_locator("get_devicesinformation")
        super().click_btn(elem)


    def devices_door(self):
        elem = self.elem_locator.get_locator("devices_door")
        return super().get_radio_button_status(elem)



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



    def language_select(self):
        try:
            # 获取元素的定位器
            elem = self.elem_locator.get_locator("language_select")

            if elem:
                # 尝试查找元素
                try:
                    found_element = self.driver.find_element(*elem)
                    # 如果找到元素，点击它
                    if found_element:
                        super().click_btn(elem)
                    else:
                        logging.error("未找到指定元素: {}".format(elem))
                        # 元素不存在时进行截图
                        screenshout_url = PubMethod.screen_picture(self.driver)
                except NoSuchElementException:
                    logging.error("NoSuchElementException: 无法找到元素: {}".format(elem))
                    # 元素不存在时进行截图
                    screenshout_url = PubMethod.screen_picture(self.driver)
            else:
                logging.error("获取元素定位器失败: {}".format(elem))
                # 定位器不存在时进行截图
                screenshout_url = PubMethod.screen_picture(self.driver)

        except Exception as e:
            logging.error(f"点击元素时出现未知错误: {str(e)}")
            # 捕获其他未知异常并进行截图
            screenshout_url = PubMethod.screen_picture(self.driver)

    def language_english(self):
        try:
            elem = self.elem_locator.get_locator("language_english")
            if elem:
                try:
                    found_element = self.driver.find_element(*elem)
                    # 如果找到元素，点击它
                    if found_element:
                         super().click_btn(elem)
                    else:
                         logging.error("未找到指定元素: {}".format(elem))
                         # 元素不存在时进行截图
                         screenshout_url = PubMethod.screen_picture(self.driver)

                except NoSuchElementException:
                   logging.error("NoSuchElementException: 无法找到元素: {}".format(elem))
                   # 元素不存在时进行截图
                   screenshout_url = PubMethod.screen_picture(self.driver)

            else:
                 logging.error("获取元素定位器失败: {}".format(elem))
                 # 定位器不存在时进行截图
                 screenshout_url = PubMethod.screen_picture(self.driver)

        except Exception as e:
               logging.error(f"点击元素时出现未知错误: {str(e)}")
               # 捕获其他未知异常并进行截图
               screenshout_url = PubMethod.screen_picture(self.driver)

    def sure_english(self):
        try:
            # 获取元素的定位器
            elem = self.elem_locator.get_locator("sure_english")

            if elem:
                # 尝试查找元素
                try:
                    found_element = self.driver.find_element(*elem)
                    # 如果找到元素，点击它
                    if found_element:
                        return super().get_text(elem)
                    else:
                        logging.error("未找到指定元素: {}".format(elem))
                        # 元素不存在时进行截图
                        screenshout_url = PubMethod.screen_picture(self.driver)
                except NoSuchElementException:
                    logging.error("NoSuchElementException: 无法找到元素: {}".format(elem))
                    # 元素不存在时进行截图
                    screenshout_url = PubMethod.screen_picture(self.driver)
            else:
                logging.error("获取元素定位器失败: {}".format(elem))
                # 定位器不存在时进行截图
                screenshout_url = PubMethod.screen_picture(self.driver)

        except Exception as e:
            logging.error(f"点击元素时出现未知错误: {str(e)}")
            # 捕获其他未知异常并进行截图
            screenshout_url = PubMethod.screen_picture(self.driver)



    def dingwei_wenbenkuang(self):
        try:
            # 获取元素的定位器
            elem = self.elem_locator.get_locator("insert_page")

            if elem:
                # 尝试查找元素
                try:
                    found_element = self.driver.find_element(*elem)
                    # 如果找到元素，清除文本
                    if found_element:
                        return super().clear_text_field(elem)
                    else:
                        logging.error("未找到指定元素: {}".format(elem))
                        # 元素不存在时进行截图
                        screenshout_url = PubMethod.screen_picture(self.driver)
                except NoSuchElementException:
                    logging.error("NoSuchElementException: 无法找到元素: {}".format(elem))
                    # 元素不存在时进行截图
                    screenshout_url = PubMethod.screen_picture(self.driver)
            else:
                logging.error("获取元素定位器失败: {}".format(elem))
                # 定位器不存在时进行截图
                screenshout_url = PubMethod.screen_picture(self.driver)

        except Exception as e:
            logging.error(f"点击元素时出现未知错误: {str(e)}")
            # 捕获其他未知异常并进行截图
            screenshout_url = PubMethod.screen_picture(self.driver)


    def input_kuang(self,value):
        try:
            # 获取元素的定位器
            elem = self.elem_locator.get_locator("input_kuang")

            if elem:
                # 尝试查找元素
                try:
                    found_element = self.driver.find_element(*elem)
                    # 如果找到元素，发送文本
                    if found_element:
                         super().send_key(elem,value)
                    else:
                        logging.error("未找到指定元素: {}".format(elem))
                        # 元素不存在时进行截图
                        screenshout_url = PubMethod.screen_picture(self.driver)
                except NoSuchElementException:
                    logging.error("NoSuchElementException: 无法找到元素: {}".format(elem))
                    # 元素不存在时进行截图
                    screenshout_url = PubMethod.screen_picture(self.driver)
            else:
                logging.error("获取元素定位器失败: {}".format(elem))
                # 定位器不存在时进行截图
                screenshout_url = PubMethod.screen_picture(self.driver)

        except Exception as e:
            logging.error(f"点击元素时出现未知错误: {str(e)}")
            # 捕获其他未知异常并进行截图
            screenshout_url = PubMethod.screen_picture(self.driver)



    # def get_toash1(self):
    #     elem = self.elem_locator.get_locator("get_toash")
    #     return super().get_text(elem)

    def get_toash1(self):
        try:
            # 获取元素的定位器
            elem = self.elem_locator.get_locator("get_toash")

            if elem:
                # 尝试查找元素
                try:
                    found_element = self.driver.find_element(*elem)
                    # 如果找到元素，获取文本
                    if found_element:
                        return super().get_text(elem)
                    else:
                        logging.error("未找到指定元素: {}".format(elem))
                        # 元素不存在时进行截图
                        screenshout_url = PubMethod.screen_picture(self.driver)
                except NoSuchElementException:
                    logging.error("NoSuchElementException: 无法找到元素: {}".format(elem))
                    # 元素不存在时进行截图
                    screenshout_url = PubMethod.screen_picture(self.driver)
            else:
                logging.error("获取元素定位器失败: {}".format(elem))
                # 定位器不存在时进行截图
                screenshout_url = PubMethod.screen_picture(self.driver)

        except Exception as e:
            logging.error(f"点击元素时出现未知错误: {str(e)}")
            # 捕获其他未知异常并进行截图
            screenshout_url = PubMethod.screen_picture(self.driver)










