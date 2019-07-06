#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   config_utils.py
@Time    :   2019/07/05 16:56:26
@Author  :   R4v3zn
@Version :   1.0
@Contact :   woo0nise@gmail.com
'''
import os
import yaml
# 配置文件名称
CONFIG_FILE_NAME = 'config.yml'
# 配置文件所处文件夹
CONFIG_FILE_FOLDER = 'config'
# 获取配置文件的绝对路径
CONFIG_FILE_PATH  = os.path.join(os.path.abspath('..'),CONFIG_FILE_FOLDER,CONFIG_FILE_NAME)
# 默认配置
DEFAULT_CONFIG = {
    'boom': {
        'concurrent':  10,
        'time_out': 10,
        'retry': 0
    }
}
'''
获取YAML配置文件中节点对应的指
:@param name 节点名称
:@return 节点值
'''
def get(name):
    config_data = get_config()
    tmp_value = None
    key_list = name.split('.')
    for key in key_list:
        if tmp_value:
            tmp_value = tmp_value[key]
        else:
            tmp_value = config_data[key]
    return tmp_value

'''
获取YAML配置文件中所有的配置信息
:@return 配置结果信息
'''
def get_config():
    config_data = {}
    with open(CONFIG_FILE_PATH) as f:
        config_data = yaml.load(f,Loader=yaml.FullLoader)
    return config_data

'''
获取YAML配置文件中节点对应的指
:@param name 节点名称
:@return Boolean，True：成功，False：失败
'''
def change(name,value):
    try:
        config_data = get_config()
        tmp_value = None
        key_list = name.split('.')
        for key in key_list[:-1]:
            if tmp_value:
                tmp_value = tmp_value[key]
            else:
                tmp_value = config_data[key]
        tmp_value[key_list[-1]] = value
        with open(CONFIG_FILE_PATH,'w') as f:
            yaml.dump(config_data,f,Dumper=yaml.Dumper)
            return True
    except Exception as e:
        return False

    
if __name__ == "__main__":
    pass
    #change('boom.time_out',10)