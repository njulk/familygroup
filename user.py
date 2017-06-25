# -*- coding: utf-8 -*-
#import MySQLdb
import web
import json as js
import MySQLdb
import time
from datetime import date
from datetime import datetime
from urls import *
from utils import *
#from urls import *
#from utils import *
#import re, chardet

# urls = (
#     '/login','login',
#     '/update','update',
#     '/gettalk','gettalk',
#     '/comment','comment',
# )




class CJsonEncoder(js.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return js.JSONEncoder.default(self, obj)




class login:            #login应该是POST请求
    def POST(self):
        data = web.data()
        self.mtransation = db.transaction()
        decodeData = js.loads(data)  #tmp为字典类型
        userid = str(decodeData['userid'])
        selectResult = list(db.select('link_user', what="userid,groupid,nickname,age,gender,charactersignature,birthday,portrait", where='userid=$userid',vars={'userid':userid}))
        #print len(selectResult)
        if len(selectResult)==0:
            registerTime = datetime.now()
            db.insert('link_user', userid=userid, registertime=registerTime)
            self.mtransation.commit()
            return js.dumps(createSuccess("register success"))
        else:
            self.mtransation.rollback()
            return js.dumps(createSuccess(selectResult),cls=CJsonEncoder)

class update:            #login应该是POST请求
    def PUT(self):
        data = web.data()
        self.mtransation = db.transaction()
        decodeData = js.loads(data)  #tmp为字典类型
        userid = str(decodeData['userid'])
        age = decodeData['age']
        name = decodeData['name']
        nickname = decodeData['nickname']
        portrait = decodeData['portrait']
        gender = decodeData['gender']
        birthday = decodeData['birthday']
        charactersignature = decodeData['charactersignature']
        #imagePath= decodeData['imagepath']

        db.update('link_user', where='userid=$userid',vars={'userid':userid}, age=age, name=name, nickname=nickname, gender=gender, birthday=birthday,charactersignature=charactersignature, portrait=portrait)
        self.mtransation.commit();
        return json.dumps(createSuccess("update success"))

# 获取了相应的talk和comment但是还没有传图片
class gettalk:
    def gettalkAcom(self,curid,eventid):
        curcomment=list(db.select('comment',where='talkid=' + curid))
        curresult={}
        curresult["talk"]= list(db.select('talk',where='eventid=' + eventid + " "+ "AND" +" "+"talkid="+curid))
        curresult['comment']=list(db.select('comment',where='talkid=' + curid))
        print(curresult)
        return curresult;
    def GET(self):
        user_data = web.input()
        self.mtransation = db.transaction()
        eventid = user_data.eventid
        talkResult = list(db.select('talk',where='eventid=' + eventid,order="time DESC",limit=10))
        talkidResult = list(db.select('talk', what="talkid", where='eventid=' + eventid, order="time DESC", limit=10))
        allcomment=[]
        for i in talkidResult:
            '''items = str(i).split(':')
            item = items[1];
            talkid_only_items = item.split('L');
            talkid_only =  talkid_only_items[0];'''
            curresult=self.gettalkAcom(str(i['talkid']),eventid)
            allcomment.append(curresult)
            # commentResult =list(db.select('comment',where='talkid=' + talkid_only,order="time DESC",limit=10))
            # allcomment.extend(commentResult);

        #talkResult.extend(allcomment)
        self.mtransation.commit();

        return js.dumps(createSuccess(list(allcomment)),cls=CJsonEncoder)

class comment:
    def POST(self):
        data = web.data()
        self.mtransation = db.transaction()
        decodeData = js.loads(data)  # tmp为字典类型
        userId = decodeData['userid']
        talkId = decodeData['talkid']
        commentText = decodeData['comment']

        mtime = time.strftime("%Y-%m-%d %H:%M:%S")
        db.insert('comment',talkid=talkId,userid=userId,commentcontent=commentText,time=mtime)
        self.mtransation.commit();
        return createSuccess("comment commit success")

class user:
    def GET(self):
        input=web.input()
        if 'userid' in input:
            userid=input.get('userid')
            array=list(db.select('link_user',where='userid=$userid',vars=locals()))
            if len(array)==0:
                res=creatFailure(5)
            else:
                res=createSuccess(array[0])
        else:
            res=creatFailure(1)

        web.header('content-type', 'text/json')
        return json.dumps(res, cls=JsonExtendEncoder)


