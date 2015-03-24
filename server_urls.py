# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:52:21 2015

@author: Jaipal Singh Goud
"""
from TardisForm.testing_dict_creator import YAMLFormHandler
import os
import tornado.template
import tornado.web

urls = [(r"/yamlform", YAMLFormHandler),(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'HTML_Static')})]