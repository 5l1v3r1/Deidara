#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mysql.py
@Time    :   2019/07/05 16:14:58
@Author  :   R4v3zn
@Version :   1.0
@Contact :   woo0nise@gmail.com
'''
import pymysql
import os
import sys
pymysql.install_as_MySQLdb()
sys.path.append(os.path.abspath('..'))
from utils import config
'''
测试连接数据库
:@param ip 测试HOST
:@param port 端口号
:@param user_name 连接用户名
:@param password 连接密码
'''
def crack(ip,port=3306,user_name='root',password='root'):
    result = {}
    try:
        conn = pymysql.connect(host=ip,port=port,user=user_name,password=password,charset="utf8")
        cursor = conn.cursor()
        cursor.execute("select version()")
        version = cursor.fetchone()[0]
        result = {
            'ip': ip,
            'port': port,
            'user_name': user_name,
            'password': password,
            'version': version
        }
    except Exception as e:
        print e
    return result

if __name__ == "__main__":
    ip = '127.0.0.1'
    port = 3306
    user_name = 'root'
    password = 'Wy599885619'
    print crack('127.0.0.1',password=password)