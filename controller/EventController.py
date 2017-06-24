# -*- coding: utf-8 -*-

import web
import json
import datetime
import uuid
import sys
sys.path.append('..')

import model.EventModel
import utils


class EventController:

    # 根据groupid获取event
    def GET(self):
        input=web.input()

        try:
            if 'groupid' in input:
                if 'pagecount' in input and 'pageindex' in input:
                    index=int(input.pageindex)
                    count=int(input.pagecount)
                    start=(index-1)*count

                    data=model.EventModel.getEventPageByGroupid(input.groupid,start,count)
                else:
                    data=model.EventModel.getEventByGroupid(input.groupid)
            else:
                data=model.EventModel.getEvents()
            res=utils.createSuccess(data)

        except: 
            res=utils.creatFailure(2)

        web.header('content-type', 'text/json')
        return json.dumps(res,cls=utils.JsonExtendEncoder)

    # 提交新的event
    def POST(self):
        input=json.loads(web.data())
        
        if 'eventname' and 'createuserid' and 'groupid' in input:
            condition={
                'createtime': datetime.datetime.utcnow(),
                'eventname': input['eventname'],
                'createuserid': input['createuserid'],
                'groupid': input['groupid'],
                'eventdescription': input.get('eventdescription'),
                'eventpicture': input.get('eventpicture')
            }

            try:
                model.EventModel.postEvent(condition)
                res=utils.createSuccess()
            except:
                res=utils.creatFailure(2)

        else:
            res=utils.creatFailure(1)

        web.header('content-type', 'text/json')
        return json.dumps(res)

    # 修改事件
    def PUT(self):
        input=json.loads(web.data())
            
        if 'eventid' in input:
            condition={
                'eventname': input.get('eventname'),
                'eventdescription': input.get('eventdescription'),
                'eventpicture': input.get('eventpicture')
            }

            try:
                model.EventModel.putEvent(input['eventid'],condition)
                res=utils.createSuccess()
            except:
                res=utils.creatFailure(2)
            
        else:
            res=utils.creatFailure(1)

        web.header('content-type', 'text/json')
        return json.dumps(res)

    # 删除事件
    def DELETE(self):
        input=web.data()

        if 'eventid' in input:
            try:
                model.EventModel.deleteEvent(input.get('eventid'))
                res=utils.createSuccess()
            except:
                res=utils.creatFailure(2)
        else:
            res=utils.creatFailure(1)

        web.header('content-type', 'text/json')
        return json.dumps(res)






