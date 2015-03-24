# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:42:41 2015

@author: troller
"""

import os
import tornado.web
import tornado.template
from yaml_parse import MakeOrderedDict
from yaml_parse import *
import yaml_parse

class YAMLFormHandler(tornado.web.RequestHandler):
    def get(self):
        source = open(os.path.join(os.path.dirname(__file__),"Tardis_config.yml")).read()
        obj = MakeOrderedDict(source)
        yaml_config = obj.parse_yaml(source)   #yaml_parsed is now an ordredDic
        self.render(
                    'Tardis_Form.html',
                    yaml_config_name='root',
                    yaml_config_dict=yaml_config,
                    generate_form=self.generate_form,
                    request_label=request_label
                    )

#    def render_form(self, yaml_config, yaml_config_name):
    def generate_form(self, yaml_config, yaml_config_name):
        return self.render_string(
                                'config_form_generator.html',
                                yaml_config_name=yaml_config_name,
                                yaml_config_dict=yaml_config,
                                generate_form=self.generate_form,
                                request_label=request_label
                                )
