# -*- coding: UTF-8 -*-
import json
from datetime import *
import time
urls=(
    '/','Home',
    '/creategroup','creategroup',   #post(/creategroup?createuserid=&groupname=&groupdescription=写在body里)
    '/updategroup','updategroup',    #put
    '/addgroup','addgroup',          #post
    '/createtalk','createtalk',      #post /createtalk?eventid=&userid=&content(写在body里)
    '/creategroupmap','creategroupmap',
    '/getgroupim','getgroupim',
    '/getgroup','getgroup',
    '/login','login',
    '/update','update',
    '/gettalk','gettalk',
    '/comment','comment',
    '/event','EventsController',
    '/event/(.+)','EventController',
    '/user','user'
)

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)



#print(json.dumps({"userid":4536,"eventid":123,"talkcontent":"adsgasg","pictureurl":"asljdkglkag"}))

