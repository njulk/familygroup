# -*- coding: utf-8 -*-

import web

import sys
sys.path.append('..')
from utils import db

t=db.transaction()

# 获取所有事件
def getEvents():
    data=db.select('event', order='eventid DESC')
    return list(data)

# 获取单一事件
def getEventById(eventid):
    data=db.select('event',where='eventid=$eventid',vars={'eventid': eventid})[0]
    return dict(data)

# 根据groupid获取事件集合
def getEventByGroupid(groupid):
    data=db.select('event',where='groupid=$groupid',vars={'groupid': groupid})
    return list(data)

# 根据groupid获取事件集合并分页
def getEventPageByGroupid(groupid,start,offset):
    data=db.select('event',where='groupid=$groupid',order='createtime desc,eventid desc', 
        limit='$start,$offset',vars=locals())
    return list(data)

# 新增事件
def postEvent(prop):
    try:
        db.insert('event',**prop)
    except:
        t.rollback()
        raise
    else:
        t.commit()

# 修改事件
def putEvent(id,prop):
    try:
        db.update('event',where='eventid=$eventid',vars={'eventid': id},**prop)
    except:
        t.rollback()
        raise
    else:
        t.commit()

# 删除事件
def deleteEvent(id):
    try:
        db.delete('event', where='eventid=$eventid',vars={'eventid': id})
    except:
        t.rollback()
        raise
    else:
        t.commit()
