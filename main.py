#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
web.config.debug = False

from controller.home import Home
from controller.EventController import *
from controller.notfound import notfound
from urls import urls
from Group import *
from talk import *
from user import *
from controller.EventController import *


app = web.application(urls, globals())
app.notfound = notfound


session = web.session.Session(
    app, web.session.DiskStore('sessions'), initializer={'login': 0})


def session_hook():
    web.ctx.session = session

app.add_processor(web.loadhook(session_hook))
    
if __name__=='__main__':
    #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()



