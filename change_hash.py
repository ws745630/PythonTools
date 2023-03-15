#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 改变文件的hash值

import sys
import getopt
import os
import subprocess
import random
import string
import sqlite3


def get_random_end():
    int_random = random.randint(32, 52)
    ret = ''.join(random.sample(
        string.ascii_letters + string.digits, int_random))
    return ret


def change_sqlite3_db_content(db_path=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    name = ''.join(random.sample(string.ascii_letters, 4))
    user = ''.join(random.sample(string.ascii_letters, 4))
    michael = ''.join(random.sample(string.ascii_letters, 7))
    cursor.execute(
        'CREATE TABLE %s (id VARCHAR(20) PRIMARY KEY, %s VARCHAR(20))' % (user, name))
    cursor.execute(
        'insert into %s (id, %s) values (\'1\', \'%s\')' % (user, name, michael))
    cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()


def run_cmd(cmd=None):
    print(cmd)
    # 返回的其实是一个编码后的比特值，实际的编码格式取决于调用的命令
    ret = subprocess.check_output(cmd, shell=True)
    return ret


def change_file_hash(project_path=None):
    os.chdir(project_path)
    file_type_array = ['*.png', '*.jpg', '*.JPG', '*.gif', '*.mp4', '*.mp3']
    for file_name in file_type_array:
        files_string = run_cmd('find . -iname "%s"' % (file_name)).decode()
        files = files_string.split('\n')
        for file in files:
            if '' == file:
                continue
            salt = get_random_end()
            run_cmd('echo "%s" >> "%s"' % (salt, file))

    db_type_array = ['*.sqlite', '*.db']
    for db_name in db_type_array:
        files_string = run_cmd('find . -iname "%s"' % (db_name)).decode()
        files = files_string.split('\n')
        for file in files:
            if '' == file:
                continue
            change_sqlite3_db_content(file)


def run():
    # 通过外部接受参数 比如：python chage_hash.py -p /Users/main/Desktop
    # opts, args = getopt.getopt(sys.argv[1:], "p:")
    # for op, value in opts:
    #     # u3d project path
    #     if op == '-p':
    #         project_path = value
    # if not project_path:
    #     print("UUProcess: no args for -p")
    change_file_hash(
        project_path="/Users/wangcl/CMUnity/Court/Assets")


if __name__ == "__main__":
    run()
