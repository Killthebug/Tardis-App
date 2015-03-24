# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:43:36 2015

@author: Jaipal Singh Goud
"""
import os
import sys
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.template
import tornado.speedups
import tornado.escape
from server_settings import settings
from server_urls import urls

webapp = tornado.web.Application( handlers=urls,**settings)

if __name__ == "__main__":
    webapp .listen(8888)
    tornado.ioloop.IOLoop.instance().start()
