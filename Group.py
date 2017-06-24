# -*- coding: UTF-8 -*-
from urls import *
import web
import json
import MySQLdb
import datetime
import random
import time
from utils import *


def producegroupid():
    ishasid=True
    while(ishasid!=False):
        result=random.randint(10,2147483647)
        id=str(result)
        if(json.dumps((list(db.select('familygroup',what='groupid',where="groupid="+ id))),cls=CJsonEncoder)!="[]"):
            continue
        else:
            ishasid=False
            return result

def getgroupinfo(mgroupid):
    mgroupid=str(mgroupid)
    data={
        'group': list(db.select('familygroup',where="groupid="+mgroupid)),
        'members': list(db.select('link_user',where="groupid="+mgroupid))
    }
    return json.dumps(createSuccess(data),cls=CJsonEncoder)



class creategroup:
    def __init__(self):
        self.mtransation=db.transaction()
    def POST(self):
        receivedata=json.loads(web.data())
        if 'createuserid'in receivedata:
            mgroupid=producegroupid()
            mcreateuserid=receivedata['createuserid']
            mgroupname =None
            mgroupdescription=None
            if 'groupname'in receivedata:
                mgroupname=receivedata['groupname']
            if "groupdescription"in receivedata:
                mgroupdescription=receivedata['groupdescription']
            mgroupportrait=None
            if "groupportrait" in receivedata:
                mgroupportrait=receivedata['groupportrait']
            msetgrouptime=time.strftime("%Y-%m-%d %H:%M:%S")
            result=json.dumps('1');
            strcreateuserid=str(mcreateuserid)
            try:
                db.insert('familygroup',groupid=mgroupid,createuserid=mcreateuserid,groupname=mgroupname,groupdescription=mgroupdescription,setgrouptime=msetgrouptime,groupportrait=mgroupportrait)
                db.update('link_user',where="userid="+strcreateuserid,groupid=mgroupid);
                #strgroupid=str(mgroupid)
                #data=list(db.select('familygroup',where="groupid="+strgroupid))
                #print(data)
                #result=json.dumps((data))
                result=getgroupinfo(mgroupid)
            except:
                self.mtransation.rollback()
                return json.dumps(creatFailure(1,u"错误"))
            else:
                self.mtransation.commit()
                return result
        else:
            return json.dumps(creatFailure(1,u"参数不全"))


class updategroup:
    def __init__(self):
        self.mtransation=db.transaction()
    def PUT(self):
        receivedata = json.loads(web.data())
        if 'groupid' in receivedata:
            mgroupid=receivedata['groupid']
        else:
            return json.dumps(creatFailure(1,u"参数不全"))
        mgroupname=None
        mgroupdescription=None
        if 'groupname' in receivedata:
            mgroupname=receivedata['groupname']
        if 'groupdescription' in receivedata:
            mgroupdescription=receivedata['groupdescription']
        mgroupportrait = None
        if "groupportrait" in receivedata:
            mgroupportrait = receivedata['groupportrait']

        strgroupid=str(mgroupid)
        try:
            db.update('familygroup',where="groupid="+strgroupid,groupname=mgroupname,groupdescription=mgroupdescription,groupportrait=mgroupportrait)
            #data=json.dumps((list(db.select('familygroup',where="groupid="+strgroupid))))
            #print(data)
        except:
            self.mtransation.rollback()
            return json.dumps(creatFailure(1,u"错误"))
        else:
            self.mtransation.commit()
            #return data
            return getgroupinfo(mgroupid)


class addgroup:
    def __init__(self):
        self.mtransation = db.transaction()
    def POST(self):
        receivedata = json.loads(web.data())
        if 'userid' and 'groupid' in receivedata:
            muserid = receivedata['userid']
            mgroupid = receivedata['groupid']
        else:
            return json.dumps(creatFailure(1,u"参数错误"))
        strgroupid=str(mgroupid)
        struserid=str(muserid)
        if(json.dumps(list(db.select('familygroup',where="groupid="+strgroupid)),cls=CJsonEncoder)=="[]"):
            return json.dumps(creatFailure(1,u"没有此组"))
        else:
            try:
                db.update('link_user', where="userid=" + struserid, groupid=mgroupid);
            except:
                self.mtransation.rollback()
                return json.dumps(creatFailure(1,u"SQL更新错误"))
            else:
                self.mtransation.commit()
                #data = json.dumps((list(db.select('familygroup', where="groupid=" + strgroupid))))
                #return data
                return getgroupinfo(mgroupid)
'''
db.insert('link_user', userid=234568, name="lk", nickname="brennanli",
          registertime="afhg")
'''



#getgroupinfo(801787497)






