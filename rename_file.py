#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 改变文件名称

import os
import glob
# 需要修改的类名前缀
pre_str = "HYJ"
# 新的类名前缀 （需替换）
pre_to_str = "RGC"

# 删除iOS中2x图片保留3x的,并去除@3x标识


def remove_ios_image(files):
    for filepath in files:
        index = filepath.find("@2x")
        if index > 0:
            os.remove(filepath)
        else:
            newfilepath = filepath.replace("@3x", "")
            os.rename(filepath, newfilepath)


if __name__ == '__main__':
    path = "/Users/wangcl/Downloads/WordGame/Assets/Resources/Images/roles"
    files = glob.glob(os.path.join(path, '*.*g'))
    remove_ios_image(files)
