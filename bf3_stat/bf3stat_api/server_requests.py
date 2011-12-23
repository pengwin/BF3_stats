"""
 Module for interaction with bf3stats.com API.
 Contains function that return json response.
 Functions with signed_ prefix use registered app ident and key for request data.
"""
__author__ = 'pengwin4'

import string
import base64
import hashlib
import hmac
from django.utils import simplejson
import httplib, urllib

import config

def request(url, post_params):
    """  Gets json response from api.bf3stats.com
    Args:
        url: string with format "/{platform}/{data_group}/" where
            {platform} can be pc, 360, ps3
            {data_group} can be player, playerlist, playerupdate, playerlookup
        pos_params: dictionary with post parameters of request
    Returns:
        Tuple : json api  response converted to dictionary, http response status,  http response reason
    """
    headers = {'Content-type': "application/x-www-form-urlencoded", 'User-Agent': "BF3StatsAPI/0.1"}
    conn = httplib.HTTPConnection("api.bf3stats.com")
    conn.request("POST", url, urllib.urlencode(post_params), headers)
    response = conn.getresponse()
    raw_data = response.read()
    conn.close()
    data_dict = simplejson.loads(raw_data)
    return data_dict, response.status, response.reason,

def _urlbase64(data):
    """ Helper function for creation urlbase64 encoded string from simple base64 string
    Args:
        data:base64 encoded string
    Returns:
        string with symbols replaced  according to pattern: '+'=>'-' ' /'=>'_' '='=>'' '\n'=>''
    """
    result = string.replace(data, '+', '-')
    result = string.replace(result, '/', '_')
    result = string.replace(result, '=', '')
    result = string.replace(result, '\n', '')
    return result

def signed_request(url,data_dict):
    """  Gets json response via signed request from api.bf3stats.com
    Args:
        url: string with format "/{platform}/{data_group}/" where
            {platform} can be pc, 360, ps3
            {data_group} can be player, playerlist,playerupdate, playerlookup
        data_dict: dictionary with request data
    Returns:
        Tuple : json api  response converted to dictionary, http response status,  http response reason
    """
    raw_data = simplejson.dumps(data_dict)

    raw_data = base64.encodestring(raw_data)
    raw_data = _urlbase64(raw_data)

    signature = base64.encodestring(hmac.new(config.BF3STATS_KEY, msg=raw_data, digestmod=hashlib.sha256).digest())
    signature = _urlbase64(signature)

    post_data = {}
    post_data['data'] = raw_data
    post_data['sig'] = signature
    return request(url, post_data)



  