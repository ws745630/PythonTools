#!/usr/bin/python3
# -*- coding: utf-8 -*-

###  iOS iMessage iCon创建
import os
from PIL import Image
import json
import time
from enum import Enum

################# 必填参数 ###############################################
#AppIcon 名称  
iConName = 'icon.png'
#生成appIcon的类型 默认生成appiCon

########################################################################
# 生成iMessage图标
def createIconFile(filePath,outPath):
    #打开本地json文件
    with open(outPath,'r') as f:
       data = json.load(f)
    print('正在生成中.......')
    #获取当前文件路径的父目录
    curPath = os.path.dirname(os.path.realpath(outPath))
    image_list = data['images']
    print('image list',image_list.count)
    for (index,imgInfo) in enumerate(image_list):
        img = Image.open(filePath)
        imageSize = imgInfo['size'].split('x')
        imageW = float(imageSize[0])
        imageH = float(imageSize[1])
        scales = imgInfo['scale'].split('x')
        scale = float(scales[0])
        
        saveWidth = int(imageW*scale)
        saveHeight = int(imageH*scale)
        #print("原始尺寸%dx%d %d，生成尺寸%dx%d"%(imageW,imageH,scale,saveWidth,saveHeight))
        #拼接filename
        if scale > 1:
            #str(imageW*scale) + 'x' + str(imageH*scale) + '@' + imgInfo['scale'] + '.png' 
           outName = '%dx%d@%s.png'%(saveWidth,saveHeight,imgInfo['scale'])
        else:
           outName = '%dx%d.png'%(imageW,imageH)

        imgInfo['filename'] = outName
        outFilePath = os.path.join(curPath,outName)
        #重设图片大小
        out = img.resize((saveWidth,saveHeight),Image.BILINEAR)
        out.save(outFilePath)
        
        print('\r','当前的进度:{0}%'.format(round((index + 1) * 100 / len(image_list))),end='',flush=True)
        #time.sleep(0.1)

    with open(outPath,'w') as f:
        json.dump(data,f)
        print("文件写入成功")

    return True
    
#删除文件   
def removeFile(filePath):
    os.remove(filePath)

#创建目录
def createMkdir(path):
    # 如果不存在则创建目录
    if not os.path.exists(path):
        os.mkdir(path)
        print('创建成功:',path)
    else:
        print('目录已存在:',path)


#如果AppIcon是透明底，就把图片的透明转为白色背景
def checkIconContainAlpha():
    print("正在检查图片是Alpha通道是否为0\n")
    _filepath = os.path.join(os.getcwd(),iConName) 
    image = Image.open(_filepath)
    if image.mode == 'RGBA':
       print("Alpha通道为0，正在转换Alpha通道\n")
       image = image.convert('RGB')
       image.save(_filepath)
       print("转换完成\n")
 

def inputFile():
   inputPath = input('请输入项目根路径:')
   fullPath = os.path.join(inputPath,detailPath)
   if not os.path.exists(fullPath):
        print('项目根目录不正确，请重新设置！！！！')
        inputFile()
   else:
        return fullPath
#获取生成icon的类型
def inputIconType():
   print("请输入生成AppIcon类型:")
   _iconType = input('1 生成AppIcon(默认) \n2 iMessageIcon:\n')
   if _iconType == "1" or _iconType == "2":
        return _iconType
   elif _iconType == "":
       return "1"
   else:
       print('输入无效！！！！')
       inputIconType()



if __name__ == '__main__':
     detailPath = ''
     iconType = inputIconType()
     if iconType == "1":
        detailPath = 'Assets.xcassets/AppIcon.appiconset/Contents.json'
        print("开始生成AppIcon")
     elif iconType == "2":
        detailPath = 'Assets.xcassets/iMessage App Icon.stickersiconset/Contents.json'
        print("开始生成iMessageIcon")
     filePath = os.path.join(os.getcwd(),iConName) 
     if not os.path.exists(filePath):
        print('没有在此目录下找到名字为',iConName)
     else:
        outPath = inputFile().strip() #去除左右空格
        checkIconContainAlpha()
        path = createIconFile(filePath,outPath)
      
        #removeFile(outPath)
        print('生成Icon成功%s\n'%(path))

   

        




