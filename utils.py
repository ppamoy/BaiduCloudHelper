# coding=utf-8
import time
import re
import zlib
import random

from gzip import GzipFile
from PIL import Image

# 兼容2.7和3.x
try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

'''
百度云引擎工具模块
'''

def get_time():
    '''
    获取当前时间戳
    
    Returns:
        string格式当前时间戳
    '''
    
    return str(int(time.time()))
    
def get_json_from_response(response):
    '''
    从response中获取json数据
    
    Args:
        response:访问返回值
    Returns:
        正则结果的list
    '''
    
    return re.findall('\(({[\s\S]*?})\)', response)

def deflate_decode(data): 
    '''
    deflate加密解码
    
    Args：
        data:加密数据
    Returns:
        解密数据
    '''
    
    try:               
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)
    
def gzip_decode(data) :  
    '''
    gzip加密解码
    
    Args：
        data:加密数据
    Returns:
        解密数据
    '''
    
    buf = StringIO(data)
    f = GzipFile(fileobj=buf)
    return f.read()

last_msg = ''
def show_msg(msg):
    global last_msg
    last_msg = msg
        
    print(msg)


def get_callback_function():
    '''
    随机生成callback函数名

    :returns: callback函数名
    '''

    list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
    return ''.join(random.sample(list, 6))

def get_gid_char(range_start):
    '''
    随机生成gid的每一位字符

    Args：
        range_start:起始范围
    Returns:
        gid字符
    '''

    char = hex(random.randint(range_start, 15))
    char = char[2:].upper()
    return char