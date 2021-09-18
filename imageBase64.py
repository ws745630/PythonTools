#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 图片转为base64

import os
import glob
import base64
import json
#### 对图片进行base64加密
## 在目录下创建一个images的文件夹把图片资源放入到此文件夹
#创建目录
def createMkdir(path):
    if not os.path.exists(path):
        # 如果不存在则创建目录
        os.mkdir(path)
        print('创建成功:',path)

def base64Code(path):
    filepath,tmpfilename = os.path.split(path)
    shortname,extension = os.path.splitext(tmpfilename)
    with open(path,"rb") as f:
         data = base64.b64encode(f.read())
    
    outpath = '%s/result'%(os.getcwd())
    createMkdir(outpath)
    out_file = '%s/%s.txt'%(outpath,shortname)
    with open(out_file,'w') as out_file:
        out_file.write(str(data, 'utf-8'))
    
if __name__ == '__main__':
    ## 获取文件内的jpg和png图片
    picture_dir = os.path.join(os.getcwd() + "/images", "*.??g")
    progress = 0
    #glob 文件名模式匹配 ！非 *所有 ？单个字符 [a-z]范围
    datafile = glob.glob(picture_dir)
    for path in datafile:
       base64Code(path)
       print('\r', '当前的进度:{0}%'.format(round((progress + 1) * 100 / len(datafile))), end='', flush=True)
       progress += 1

