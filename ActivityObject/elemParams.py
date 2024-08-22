# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/30 11:11
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : run.py
# @Software: PyCharm

import os

from Common.publicMethod import PubMethod
import logging
from selenium.webdriver.common.by import By
from Base.baseBy import BaseBy

pub_api = PubMethod()
root_dir = os.path.dirname(os.path.dirname(__file__))
config_path = os.path.join(root_dir, 'ActivityObject')
config_path = os.path.abspath(config_path)


class ElemParams:
    def __init__(self, dir_name, file_name, root_dir_name=config_path):
        self.elem_name = []
        self.desc = []
        self.data = []
        self.info = []
        self.__run(dir_name, root_dir_name, file_name)

    def __run(self, dir_name, root_dir_name, file_name):
        config_dir_name = os.path.join(root_dir_name, dir_name)
        file_path = os.path.abspath(os.path.join(config_dir_name, file_name))
        try:

            self.info = PubMethod().read_yaml(file_path)['parameters']
            for i in self.info:
                self.elem_name.append(i['elem_name'])
                self.desc.append(i['desc'])
                self.data.append(i['data'])
        except Exception as e:
            logging.error("文件解析失败！{},文件路径：{}".format(e, file_path))

    def get_locator(self, elem_name):
        elems_info = self.info

        for item in elems_info:
            if item["elem_name"] == elem_name:
                method = item["data"]["method"]
                value = item["data"]["value"]
                logging.info("元素名称为：{}，元素定位方式为：{}，元素对象值为：{}".format(elem_name, method, value))

                locator_dict = {
                    "ID": By.ID,
                    "XPATH": By.XPATH,
                    "LINK_TEXT": By.LINK_TEXT,
                    "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
                    "NAME": By.NAME,
                    "TAG_NAME": By.TAG_NAME,
                    "CLASS_NAME": By.CLASS_NAME,
                    "CSS_SELECTOR": By.CSS_SELECTOR,
                    "IOS_UIAUTOMATION": BaseBy.IOS_UIAUTOMATION,
                    "IOS_PREDICATE": BaseBy.IOS_PREDICATE,
                    "IOS_CLASS_CHAIN": BaseBy.IOS_CLASS_CHAIN,
                    "ANDROID_UIAUTOMATOR": BaseBy.ANDROID_UIAUTOMATOR,
                    "ANDROID_VIEWTAG": BaseBy.ANDROID_VIEWTAG,
                    "WINDOWS_UI_AUTOMATION": BaseBy.WINDOWS_UI_AUTOMATION,
                    "ACCESSIBILITY_ID": BaseBy.ACCESSIBILITY_ID,
                    "IMAGE": BaseBy.IMAGE,
                    "CUSTOM": BaseBy.CUSTOM
                }

                if method in locator_dict and value is not None:
                    return (locator_dict[method], value)
                else:
                    logging.error("元素名称：{}，此元素定位方式异常，定位元素值异常，请检查！！！".format(elem_name))
                    return None


# 注册login_activity_yaml文件对象
class LoginActivityElem(ElemParams):
    def __init__(self):
        super(LoginActivityElem, self).__init__('Login_activity', 'Login_activity.yaml')

# 注册Mima.yaml文件对象
class MimeActivityElem(ElemParams):
    def __init__(self):
        super(MimeActivityElem, self).__init__('Mime_activity', 'Mime.yaml')


# 注册Home_activity.yaml文件对象
class HomeActivityElem(ElemParams):
    def __init__(self):
        super(HomeActivityElem, self).__init__('Home_activity', 'Home_activity.yaml')


if __name__ == '__main__':
    login_activity = LoginActivityElem()
    print(login_activity.get_locator("phone_number"))
    mimeactivity = MimeActivityElem()
    print(mimeactivity.get_locator("mine_btn"))
    homeactivity = HomeActivityElem()
    print(homeactivity.get_locator("mine_btn"))
