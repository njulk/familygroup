#!/usr/bin/Python
# -*- coding: utf-8 -*-

import web
import json
import decimal 
from datetime import date  
from datetime import datetime

isCheckLogin=False

errors=[
    u'成功',            #0
    u'缺少必须的数据',   #1
    u'数据库操作失败',   #2
    u'数据格式错误',     #3
    u'没有权限',         #4
    u'此ID不存在'        #5
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

# 进行权限验证
def logged(func):
    def wrapper(*args,**kw):
        if web.ctx.session.login==1 or not isCheckLogin:
            return func(*args,**kw)
        else:
            res=creatFailure(4)
            return json.dumps(res)
    return wrapper
            


# db=web.database(dbn='mysql',user='root',pw='123456789',db='family',host="localhost")
db=web.database(dbn='mysql',user='cdb_outerroot',pw='w85685216',db='familygroup',port=8470,host="594d02b639e4a.gz.cdb.myqcloud.com")