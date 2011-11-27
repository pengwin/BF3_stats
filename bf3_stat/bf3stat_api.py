__author__ = 'pengwin4'

# Module for interaction with bf3stats.com API.
# Contains function that return json response.
# For information about structure of response and request parameters look bf3stats.com/api
# Partially objects for player data are represented in 'models.py'.
# Relation between this objects and json data can be found in 'player_crud.py'.
# Functions with signed_ prefix use registered app ident and key for request data.

import string
import time
import base64
import hashlib
import hmac
from django.utils import simplejson
import httplib, urllib

import bf3stat_api_config

_bf3stats_ident = bf3stat_api_config.ident # could be your ident string for registered app
_bf3stats_key = bf3stat_api_config.key # could be your key string  for registered app

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

    signature = base64.encodestring(hmac.new(_bf3stats_key, msg=raw_data, digestmod=hashlib.sha256).digest())
    signature = _urlbase64(signature)

    post_data = {}
    post_data['data'] = raw_data
    post_data['sig'] = signature
    return request(url, post_data)


def request_player_awards(player_name):
    """    Gets player statistics from server
    Args:
        player_name: no comments
    Returns:
        Tuple: json api  player data converted to dictionary, http response status,  http response reason
    """
    opts = "clear,awards,rank,scores,awardsInfo" # default request options
    params = {'opt': opts, 'player': player_name}
    url = "/{platform}/{data_group}/".format(platform="pc", data_group="player")
    return request(url, params)

def signed_request_player_update(player_name):
    """  Request player update on server
    Args:
        player_name: no comments
    Returns:
        Tuple: json api  server request  converted to dictionary, http response status,  http response reason
    """
    data_dict = {}
    data_dict['ident'] = _bf3stats_ident
    data_dict['time'] = int(time.time())
    data_dict['player'] = player_name

    url = "/{platform}/{data_group}/".format(platform="pc", data_group="playerupdate")
    return signed_request(url, data_dict)
  