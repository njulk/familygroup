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


class creategroupmap:
    def __init__(self):
        self.mtransation=db.transaction()
    def POST(self):
        #print(web.data())
        receivedata=json.loads(web.data())
        #print(receivedata)
        mgroupid=receivedata['groupid']
        mimid=receivedata['imid']
        try:
            db.insert('mapgroupid',groupid=mgroupid,imid=mimid)
        except:
            self.mtransation.rollback()
            return json.dumps(creatFailure(2,"fail"))
        else:
            self.mtransation.commit()
            return json.dumps(createSuccess("success"))


class getgroupim:
    def GET(self):
        receivedata=web.input()
        mgoupid=receivedata['groupid']
        result=[]
        try:
            result=list(db.select('mapgroupid',where="groupid="+mgoupid))
            #print(result)
            try:
                first = result[0]
            except:
                return json.dumps(creatFailure(5, "no di"))
        except:
            return json.dumps(creatFailure(2, "fail"))
        else:
            return json.dumps(createSuccess(result))

class getgroup:
    def __init__(self):
        self.mtransation = db.transaction()
    def GET(self):
        receivedata=web.input()
        mgroupid=receivedata['groupid']
        result=db.select('familygroup',where="groupid="+mgroupid)
        try:
            first=result[0]
        except:
            return json.dumps(creatFailure(5, "no id"))
        return getgroupinfo(mgroupid)



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
                db.update('link_user',where='userid=$strcreateuserid',vars={'strcreateuserid':strcreateuserid},groupid=mgroupid);
                #strgroupid=str(mgroupid)
                #data=list(db.select('familygroup',where="groupid="+strgroupid))
                #print(data)
                #result=json.dumps((data))
                result=getgroupinfo(mgroupid)
            except:
                self.mtransation.rollback()
                return json.dumps(creatFailure(2))
            else:
                self.mtransation.commit()
                return result
        else:
            return json.dumps(creatFailure(1))


class updategroup:
    def __init__(self):
        self.mtransation=db.transaction()
    def PUT(self):
        receivedata = json.loads(web.data())
        if 'groupid' in receivedata:
            mgroupid=receivedata['groupid']
        else:
            return json.dumps(creatFailure(1))
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
            return json.dumps(creatFailure(2))
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
            muserid = receivedata.get('userid')
            mgroupid = receivedata.get('groupid')
        else:
            return json.dumps(creatFailure(1))
        strgroupid=str(mgroupid)
        struserid=str(muserid)
        if(json.dumps(list(db.select('familygroup',where="groupid="+strgroupid)),cls=CJsonEncoder)=="[]"):
            return json.dumps(creatFailure(5))
        else:
            try:
                db.update('link_user', where='userid=$struserid',vars={'struserid':struserid}, groupid=mgroupid);
            except:
                self.mtransation.rollback()
                return json.dumps(creatFailure(2))
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






