# -*- coding: utf-8 -*-

import web
import json

import sys
sys.path.append('..')

import utils
import model.ReminderModel


class ReminderController:
    def GET(self,id):
        try:
            data=model.ReminderModel.getReminderById(id)
            res=utils.createSuccess(data)
        except:
            res=utils.creatFailure(2)
        
        web.header('content-type', 'text/json')
        return json.dumps(res,cls=utils.JsonExtendEncoder)

    def PUT(self,id):
        input=json.loads(web.data())
        condition={
            'title': input.get('title'),
            'content': input.get('content'),
            'remindtime': input.get('remindtime')
        }
        
        try:
            model.ReminderModel.putReminder(id,condition)
            data=model.ReminderModel.getReminderById(id)
            res=utils.createSuccess(data)
        except:
            res=utils.creatFailure(2)
        
        web.header('content-type', 'text/json')
        return json.dumps(res,cls=utils.JsonExtendEncoder)