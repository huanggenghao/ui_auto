# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/2 21:11
# @Author  : huanggenghao
# @Email   : 877649270@qq.com
# @File    : run.py
# @Software: PyCharm
import os


class File_option:
    @staticmethod
    def file_mkdir(filepath):
        if not os.path.exists(filepath):
            os.mkdir(filepath)
        else:
            print("{}目录已存在，不需要再次创建".format(filepath))

