# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:16:19 2015

@author: Jaipal Singh Goud
"""

import os
import re
import tornado
import sys

settings = dict(
    static_path =os.path.join(os.path.dirname(__file__), "HTML_Static") ,
    template_path = os.path.join(os.path.dirname(__file__), "HTML_Template"),
    login_url = "/login",    
    cookie_secret = "Random Cookie Data",
    xsrf_cookies = True,
    debug = True,
    #compiled_template_cache = False
    )
    