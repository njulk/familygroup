# -*- coding: UTF-8 -*-
from urls import *
import web
import json
import MySQLdb
import datetime
import random
import time
from utils import *



def producetalkid():
    ishasid=True
    while(ishasid!=False):
        result=random.randint(10,2147483647)
        id=str(result)
        if(json.dumps((list(db.select('talk',what='talkid',where="talkid="+ id))))!="[]"):
            continue
        else:
            ishasid=False
            return result



class createtalk:
    def __init__(self):
        self.mtransation = db.transaction()

    def POST(self):
        receivedata = json.loads(web.data())
        if "userid" and "eventid" and "talkcontent" in receivedata:
            muserid=receivedata['userid']
            meventid=receivedata['eventid']
            #mtalkid=producetalkid()
            mcontent=receivedata['talkcontent']
            mtime=datetime.now()
            mpictureurl=None
            if "pictureurl" in receivedata:
                mpictureurl=receivedata['pictureurl']
            result=json.dumps("createtalk fails")
            try:
                db.insert('talk',eventid=meventid,userid=muserid,talkcontent=mcontent,time=mtime,pictureurl=mpictureurl)
            except:
                self.mtransation.rollback()
                return json.dumps(creatFailure(2))
            else:
                self.mtransation.commit()
                streventid=str(meventid)
                struserid=str(muserid)
                return json.dumps(createSuccess(list(db.select('talk',where="eventid="+streventid+" "+"AND"+" "+"userid=$struserid"+" order by talkid desc"+" "+"LIMIT 1",vars={"struserid":struserid}))),cls=CJsonEncoder)
        else:
            return json.dumps(creatFailure(1))
