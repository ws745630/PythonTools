#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : 2.py
# @Author: huifer
# @Date : 2018/12/20
from PIL import Image
import os


def read(path, files):
    file_list = files
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)
    pic_name.sort()
    new_pic = []
    for x in pic_name:
        if "jpg" in x:
            new_pic.append(x)
    for x in pic_name:
        if "png" in x:
            new_pic.append(x)
    print("hec", new_pic)
    im1 = Image.open(os.path.join(path, new_pic[0]))
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open(os.path.join(path, i))
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)

    im1.save(path + ".pdf", "PDF", resolution=100.0,
             save_all=True, append_images=im_list)
    print("输出文件名称路径：", path + ".pdf")


if __name__ == '__main__':
    dirpath = "/Users/wangcl/Downloads/健身教练"
    for (root, dirs, files) in os.walk(dirpath):
        if len(files) > 0:
            read(root, files)
