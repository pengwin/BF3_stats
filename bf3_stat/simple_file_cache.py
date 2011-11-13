# -*- coding: utf-8 -*-
'''
Created on Nov 5, 2011

@author: ivan
'''

import os
from django.utils import simplejson

cache_path = os.path.join(os.path.dirname(__file__), 'cache').replace('\\','/')

def _get_path(player_name):
    return u"{0}/{1}.cached".format(cache_path,player_name)

def if_exists(player_name):
    path_to_file = _get_path(player_name)
    return os.path.isfile(path_to_file)

def put(player_name,data):
    path_to_file = _get_path(player_name)
    try:
        f = open(path_to_file,'w')
        str_data = simplejson.dumps(data)
        f.write(str_data)
    except IOError:
        return False
    return True

def get(player_name):
    path_to_file = _get_path(player_name)
    try:
        f = open(path_to_file,'r')
        str_data = f.read()
        data = simplejson.loads(str_data)
    except IOError:
        return None
    return data

def delete(player_name):
    if if_exists(player_name):
        path_to_file = _get_path(player_name)
        os.remove(path_to_file)

if __name__ == "__main__":
    print cache_path
    put('tt',{'name': 'TT','tt':125})
    data = get('tt')
    print data['name']
        
     
    