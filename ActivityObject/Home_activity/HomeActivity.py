# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/22 14:18
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : HomeActivity.py
# @Software: PyCharm
import logging

from selenium.common import NoSuchElementException

from Base.base import Base
from ActivityObject.elemParams import  HomeActivityElem
from Common.publicMethod import PubMethod
# 封装绿联app登录页面操作对象操作方法
class HomeActivity(Base):
    def __init__(self, driver):
        # 初始化页面元素对象，即yaml文件对象
        self.elem_locator = HomeActivityElem()
        # 初始化driver
        super().__init__(driver)


    def person_logo(self):
        try:
            # 获取元素的定位器
            elem = self.elem_locator.get_locator("person_logo")

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


    def language_select(self):
        try:
            # 获取元素的定位器
            elem = self.elem_locator.get_locator("language_select")

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