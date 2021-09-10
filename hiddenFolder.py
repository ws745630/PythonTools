#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 隐藏/显示 Mac隐藏文件夹

import os
import subprocess


def run_command(cmd):
    os.system(cmd)

# read 读取当前文件夹的状态  write 写入值 value 控制显示隐藏 隐藏文件夹
def get_command(key, value=""):
    return "defaults %s com.apple.finder AppleShowAllFiles %s" % (key, value)


if __name__ == '__main__':
    
    os.access()
    #cmd =  "ls %s"%(path)
    # 读取当前文件夹的状态：FALSE 为不显示隐藏文件夹  TRUE显示隐藏文件夹
    result = subprocess.getoutput(get_command("read"))
    if result == "FALSE":
        run_command(get_command("write", "TRUE"))
    else:
        run_command(get_command("write", "FALSE"))
    # 执行命令后重启Finder 生效
    run_command("killall Finder")
#    run_command()
