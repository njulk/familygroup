#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from controller.home import Home
from controller.EventController import *
from controller.notfound import notfound
from urls import urls
from Group import *
from talk import *
from user import *
from controller.EventController import *


app=web.application(urls,globals())
app.notfound=notfound

if __name__=='__main__':
    #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()


