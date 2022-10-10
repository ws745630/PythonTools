#!/usr/bin/python3
# -*- coding: utf-8 -*-
# iOS iMessage iCon创建

import os
from PIL import Image
import json
import time
from enum import Enum

################# 必填参数 ###############################################
# AppIcon 名称
iConName = 'icon.png'
# 使用完毕后如果不需要是要设为空
iMessageName = ""
# 生成appIcon的类型 默认生成appiCon

########################################################################
# 生成iMessage图标


def createIconFile(ico1nPath, outPath):
    # 打开本地json文件
    with open(outPath, 'r') as f:
        data = json.load(f)
    print('正在生成中.......')
    # 获取当前文件路径的父目录
    curPath = os.path.dirname(os.path.realpath(outPath))
    image_list = data['images']
    print('image list', image_list.count)
    for (index, imgInfo) in enumerate(image_list):
        img = Image.open(iconPath)
        imageSize = imgInfo['size'].split('x')
        imageW = float(imageSize[0])
        imageH = float(imageSize[1])
        scales = imgInfo['scale'].split('x')
        scale = float(scales[0])

        saveWidth = int(imageW*scale)
        saveHeight = int(imageH*scale)
        #print("原始尺寸%dx%d %d，生成尺寸%dx%d"%(imageW,imageH,scale,saveWidth,saveHeight))
        # 拼接filename
        if scale > 1:
            #str(imageW*scale) + 'x' + str(imageH*scale) + '@' + imgInfo['scale'] + '.png'
            outName = '%dx%d@%s.png' % (saveWidth,
                                        saveHeight, imgInfo['scale'])
        else:
            outName = '%dx%d.png' % (imageW, imageH)

        imgInfo['filename'] = outName
        outFilePath = os.path.join(curPath, outName)
        # 重设图片大小
        out = img.resize((saveWidth, saveHeight), Image.BILINEAR)
        out.save(outFilePath)

        print('\r', '当前的进度:{0}%'.format(
            round((index + 1) * 100 / len(image_list))), end='', flush=True)
        # time.sleep(0.1)

    with open(outPath, 'w') as f:
        json.dump(data, f)
        print("文件写入成功")

    return outPath

# 删除文件


def removeFile(filePath):
    os.remove(filePath)

# 创建目录


def createMkdir(path):
    # 如果不存在则创建目录
    if not os.path.exists(path):
        os.mkdir(path)
        print('创建成功:', path)
    else:
        print('目录已存在:', path)


# 如果AppIcon是透明底，就把图片的透明转为白色背景
def checkIconContainAlpha():
    print("正在检查图片是Alpha通道是否为0\n")
    _filepath = os.path.join(os.getcwd(), iConName)
    image = Image.open(_filepath)
    if image.mode == 'RGBA':
        print("Alpha通道为0，正在转换Alpha通道\n")
        image = image.convert('RGB')
        image.save(_filepath)
        print("转换完成\n")

# 获取输出文件路径


def inputFile(iconType):
    global inputPath
    inputPath = input('请输入项目根路径:').strip()  # 去除左右空格
    _fullPath = getOutPath(iconType, inputPath)
    if not os.path.exists(_fullPath):
        print('项目根目录不正确，请重新设置！！！！')
        inputFile(iconType)
    else:
        return _fullPath


# 获取文件的目录
def getOutPath(iconType, path, reRun=False):
    _app_path = 'Assets.xcassets/AppIcon.appiconset/Contents.json'
    _msg_path = 'Assets.xcassets/iMessage App Icon.stickersiconset/Contents.json'
    if iconType == "1":
        print("开始生成AppIcon")
        return os.path.join(path, _app_path)
    elif iconType == "2":
        print("开始生成iMessageIcon")
        return os.path.join(path, _msg_path)
    elif iconType == "3":
        if reRun:
            print("开始生成iMessageIcon")
            # 这里修改iMessage目录名称;使用#注释代码

            if len(iMessageName) > 0:
                _subixpath = iMessageName
            else:
                os.path.basename(path) + "Message"

            _prefixpath = os.path.join(path, _subixpath)
            return os.path.join(_prefixpath, _msg_path)
        else:
            print("开始生成AppIcon")
            _prefixpath = os.path.join(path, os.path.basename(path))
            return os.path.join(_prefixpath, _app_path)

# 获取生成icon的路径，reRun是否再次执行


def inputIconType():
    print("请输入生成AppIcon类型:")
    _iconType = input(
        '1 生成AppIcon(默认) \n2 iMessageIcon:\n3 同时生成AppIcon和iMessageIcon:\n')
    if _iconType == "1" or "2" or "3":
        return _iconType
    elif _iconType == "":
        return "1"
    else:
        print('输入无效！！！！')
        inputIconType()


if __name__ == '__main__':
    inputPath = ''
    iconPath = os.path.join(os.getcwd(), iConName)
    iconType = inputIconType()
    if not os.path.exists(iconPath):
        print('没有在此目录下找到名字为', iConName)
    else:
        outPath = inputFile(iconType)
        checkIconContainAlpha()
        path = createIconFile(iconPath, outPath)
        if iconType == "3":
            msgpath = getOutPath(iconType, inputPath, True)
            createIconFile(iconPath, msgpath)
        # removeFile(outPath)
        print('生成Icon成功%s\n' % (path))
