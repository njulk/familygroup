#!/usr/bin/Python
# -*- coding: utf-8 -*-

import web
import json
import decimal 
from datetime import date  
from datetime import datetime   

errors=[
    u'成功',
    u'缺少必须的数据',
    u'数据库操作失败',
    u'数据格式错误',
    u'没有权限'
]

def createSuccess(data=None):
    return {
        'code': 0,
        'message': errors[0],
        'data': data
    }

def creatFailure(code,message=None):
    if message:
        return {
            'code': code,
            'message': message
        }
    else:
        return {
            'code': code,
            'message': errors[code]
        }
   
    

# 上传图片
# def uploadImage(image,name):
#     filepath=image.filename.replace('\\','/')
#     filename=filepath.split('/')[-1]
#     ext=filename.split('.',1)[1]

#     if ext=='jpg' or ext=='png' or ext=='gif':
#         try:
#             fout=open(name+'.'+ext,'wb')
#             fout.write(image.file.read())
#             fout.close()
#             return True
#         except:
#             return False
#     else: 
#         return False

class JsonExtendEncoder(json.JSONEncoder):  
    """  
        This class provide an extension to json serialization for datetime/date.  
    """  
    def default(self, o):  
        """  
            provide a interface for datetime/date  
        """  
        if isinstance(o, datetime):  
            return o.strftime('%Y-%m-%d %H:%M:%S')  
        elif isinstance(o, date):  
            return o.strftime('%Y-%m-%d')  
        else:  
            return json.JSONEncoder.default(self, o)

# db=web.database(dbn='mysql',user='root',pw='123456789',db='family',host="localhost")
db=web.database(dbn='mysql',user='cdb_outerroot',pw='w85685216',db='familygroup',port=8470,host="594d02b639e4a.gz.cdb.myqcloud.com")