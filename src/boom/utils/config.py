#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2019/07/05 17:57:14
@Author  :   R4v3zn
@Version :   1.0
@Contact :   woo0nise@gmail.com
'''
from config_utils import *

'''
获取连接超时时间
:@return 连接超时时间
'''
def get_time_out():
    return get('boom.time_out')

'''
获取Boom中并发数量
'''
def get_concurrent():
    return get('boom.concurrent')

'''
获取Boom中重试次数
:@return 重试次数
'''
def get_retry():
    return get('boom.retry')
