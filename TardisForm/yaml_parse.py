# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 2015

@author: Jaipal Singh Goud
"""

try:
    import yaml,yaml.constructor             #Try to import the yaml package
except ImportError: 
    raise ImportError("""yaml could not be imported .
    Retry with : sudo apt-get install python-yaml """)
    
try:
    from collections import OrderedDict      #Try to import the OrderedDict
except ImportError:
    raise ImportError(""" Ordered Dict Not available """)
    
class MakeOrderedDict(yaml.Loader):
    def __init__(self, *arg, **kwarg):
        yaml.Loader.__init__(self, *arg, **kwarg)
 
        self.add_constructor(u'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(u'tag:tadis_config_file,2002:omap', type(self).construct_yaml_map)
       
    def construct_yaml_map(self, node):
        final_data = OrderedDict()            #Initialize an orderedDict
        yield final_data
        value = self.construct_mapping(node)  #Call function to map keys to the data
        final_data.update(value)              #Update returned value to the final_data
 
    def construct_mapping(self, node):
        deep = False
        if isinstance(node,yaml.MappingNode): #Check if node is a valid Mapping Node
            self.flatten_mapping(node)        #Generate mapping for the node
        else:
            raise yaml.constructor.ConstructorError("Node is not a valid yaml.MappingNode")
 
        mapping = OrderedDict()
        for key_nodes, value_nodes in node.value: #Iterate through all key and data nodes to map them
            key = self.construct_object(key_nodes, deep=deep)
            try:
                hash(key)
            except TypeError, exc:
                raise yaml.constructor.ConstructorError('Unacceptable key found (%s)' % exc, key_nodes.start_mark)
            value = self.construct_object(value_nodes, deep=deep)
            mapping[key] = value
        return mapping
   
#def load(*args, **kwargs):
  #  kwargs['Loader'] = MakeOrderedDict
  #  res = yaml.load(*args, **kwargs)
  #  return res

#def dump(*args, **kwargs):
 #   return yaml.dump(*args, **kwargs)
    
    def parse_yaml(self,source):
        #sample = file("Tardis_config.yml","r")
        try:
            import textwrap
            tardis_config = yaml.load(textwrap.dedent(source), MakeOrderedDict) #Textwrap.dedent() is used to clean off any extra spaces
        except:
            tardis_config = yaml.load(source,MakeOrderedDict)                   #If textwrap not found
            pass
    
        assert type(tardis_config) is OrderedDict   #Make sure file returned is an Ordered Dictionary
        return tardis_config
        

def request_label(label):
    return label.replace('_',' ').capitalize()
