"""

"""
__author__ = 'pengwin4'

import socket
import bf3_stat.bf3stat_api as api
import bf3_stat.dict_2_model.player
from player_exceptions import PlayerNotFound,PlayerRequestError
from bf3_stat.models import Player



def get_player(player_name):
    """
     Gets dict information about player
    Args:
        player_name:
    Returns:
        dictionary with data
    Throws:
        PlayerNotFound, RequestError
    """
    try:
        player = Player.objects.get(name=player_name) # gets from db first
    except Player.DoesNotExist:
        player = None

    try:
        data_dict, response_status, response_reason = api.request_player_awards(player_name) # loads from server
    except socket.gaierror as ex:
        raise PlayerRequestError(0,'EAI Error {0} {1}: '.format(ex[0],ex[1]))
    if response_status != 200:  # if  errors on server occurred
        raise PlayerRequestError(response_status, response_reason)
    if data_dict['status'] == u'error':
        raise PlayerRequestError('Server error',data_dict['error'])
    if data_dict['status'] == u'notfound' or data_dict['status'] == u'pifound': # if player not found on server
        raise PlayerNotFound()
    player = bf3_stat.dict_2_model.player.update_player(data_dict) # puts to db
    return player


