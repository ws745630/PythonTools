#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PIL import Image
import subprocess
import platform
import glob
import tinify
import json


###### 图片压缩 ########
# 必填参数

# tinify压缩每月只能使用500次
tinify.key = 'MgVVmK8nVYWDkfT5kb0jZ7YMqbZTLLhS'

# 获取输出文件


def get_outfile(outpath, name):
    # outfile = '{}-out{}'.format(dir, suffix)
    if not os.path.exists(outpath):
        os.mkdir(outpath)

    return os.path.join(outpath, name)

# 打开文件夹


def open_folder(path):
    # 获取系统标志
    userPlatform = platform.system()
    if userPlatform == 'Darwin':  # mac
        subprocess.call(['open', path])
    elif userPlatform == 'Linux':  # Linux
        subprocess.call(['xdg-open', path])
    else:
        os.startfile(path) 	     # Windows

# 获取文件大小


def get_size(file):
    # 获取文件大小:B
    size = os.path.getsize(file)
    return size / 1024

# 压缩图片 infile图片路径 outfile 图片输出路径   kb压缩的大小


def image_compress(infile, outfile):
    # if path isn't a image file,return
    if not infile.split('.')[-1:][0] in ['png', 'jpg', 'jpeg']:
        return
    if os.path.isdir(infile):
        return
    img = Image.open(infile)
    img.save(outfile, quality=80, optimize=True, progressive=True)  # 转换就是直接另存为


# 按比例更改图片大小
def image_compress_scale(infile, outfile, scale=0.8):
    img = Image.open(infile)
    img_w, img_h = img.size
    out = img.resize((int(img_w * scale), int(img_h * scale)), Image.BILINEAR)
    out.save(outfile)
    print('改变后的大小:width:%d height:%d' %
          (int(img_w * scale), int(img_h * scale)))
    return outfile

# 使用tinify压缩


def tinify_compress(infile, outfile):
    tinify.from_file(infile).to_file(outfile)

# 重命名文件


def rename_file(images, file_name):
    name_list = []
    for (index, tfile) in enumerate(images):
        new_name = "%s%s.png" % (file_name + index)
        old_name = os.path.basename(tfile)
        new_file = tfile.replace(old_name, new_name)
        os.rename(tfile, new_file)
        nameInfo = {'old_name': old_name, 'new_name': new_name}
        name_list.append(nameInfo)

# 写入json文件


def write_data(path, name, msg):
    full_path = path + name + '.json'  # 也可以创建一个.doc的word文档
    content = json.dumps(msg)
    with open(full_path, 'a+') as file:
        file.write(content)


def inputFile(txt):
    inputPath = input(txt).strip()
    if not os.path.exists(inputPath):
        print('路径不正确,请重新设置！！！！')
        inputFile(txt)
    else:
        return inputPath


if __name__ == '__main__':
    # 过滤图片的文件名
    inpath = inputFile('请输入项目根路径:')
    # 压缩方式 0:defaule  1:tinify 2:按照比例缩小图片
    compressType = input('请输入压缩方式:0:defaule(默认) 1:tinify 2:按照比例缩小图片') or '0'
    if int(compressType) > 3:
        print("压缩方式不正确，重新输入")
        compressType = input('请输入压缩方式:0:defaule  1:tinify 2:按照比例缩小图片')

    images = glob.glob(os.path.join(inpath, '*.*g'))
    images.sort()
    # rename_file(images)

    for (index, tfile) in enumerate(images):
        #outfile = tfile.replace('clothing','images')
        if compressType == '0':
            image_compress(tfile, tfile)
        elif compressType == '1':
            tinify_compress(tfile, tfile)
        else:
            image_compress_scale(tfile, tfile)

        print('\r', '当前的进度:{0}%'.format(
            round((index + 1) * 100 / len(images))), end='', flush=True)

    # open_folder(outpath)
