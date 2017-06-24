# -*- coding: utf-8 -*-

import web

import sys
sys.path.append('..')
from utils import db

t=db.transaction()

# 根据reminderid获取提醒
def getReminderById(id):
    data=db.select('reminder',where='reminderid=$id',vars=locals())[0]
    return dict(data)

# 根据createuserid获取提醒
def getRemindersByCreateuserid(createuserid):
    data=db.select('reminder',where='createuserid=$createuserid',vars=locals())
    return list(data)

# 新增提醒
def postReminder(prop):
    try:
        insertid=db.insert('reminder',**prop)
    except:
        t.rollback()
        raise
    else:
        t.commit()
        return insertid

# 修改提醒
def putReminder(id,prop):
    try:
        updateid=db.update('reminder',where='reminderid=$reminderid',vars={'reminderid': id},**prop)
    except:
        t.rollback()
        raise
    else:
        t.commit()
        return updateid

# 删除提醒
def deleteReminder(id):
    try:
        deleteid=db.delete('reminder', where='reminderid=$id',vars=locals())
    except:
        t.rollback()
        raise
    else:
        t.commit()
        return deleteid






