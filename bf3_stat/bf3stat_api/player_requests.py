"""
 Functions to obtain player statistics and request player update/lookup on server
 Contains function that return json response.
 Functions with signed_ prefix use registered app ident and key for request data.
"""
__author__ = 'pengwin4'

import time

import config
from server_requests import request,signed_request

def request_player(player_name,opts,platform='pc'):
    """    Gets player statistics from server
    Args:
        opts: request options string
        player_name: no comments
        platform: 'pc', '360', 'ps3'
    Returns:
        Tuple: json api  player data converted to dictionary, http response status,  http response reason
    """
    params = {'opt': opts, 'player': player_name}
    url = "/{platform}/{data_group}/".format(platform=platform, data_group="player")
    return request(url, params)

def request_player_awards(player_name):
    """    Gets player's awards info from server
    Args:
        player_name: no comments
    Returns:
        Tuple: json api  player data converted to dictionary, http response status,  http response reason
    """
    opts="clear,rank,awards,nozero,awardsInfo"
    return request_player(player_name,opts)

def signed_request_player_update(player_name,platform='pc'):
    """  Request player update on server.
    According to description on bf3stats api if np player exists server will make lookup
    Args:
        player_name: no comments
    Returns:
        Tuple: json api  server request  converted to dictionary, http response status,  http response reason
    """
    data_dict = {}
    data_dict['ident'] = config.BF3STATS_IDENT
    data_dict['time'] = int(time.time())
    data_dict['player'] = player_name

    url = "/{platform}/{data_group}/".format(platform=platform, data_group="playerupdate")
    return signed_request(url, data_dict)
  