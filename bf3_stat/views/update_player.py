__author__ = 'pengwin4'

import socket
from bf3_stat.models import PlayerUpdateStatus
from player_exceptions import PlayerNotFound,PlayerRequestError

from bf3_stat.bf3stat_api.player_requests import signed_request_player_update

def update_player(player_name):
    """
    Ags:
        player_name: player needed to update
    Returns:
        models.PlayerUpdateStatus instance
    Throws:
        PlayerNotFound, RequestError
    """
    try:
        raw_data, response_status, response_reason =  signed_request_player_update(player_name)
    except socket.gaierror as ex:
        raise PlayerRequestError(0,'EAI Error {0} {1}: '.format(ex[0],ex[1]))
    if response_status != 200:  # if  errors on server occurred
        raise PlayerRequestError(response_status, response_reason)
    if raw_data['status'] == u'error':
        raise PlayerRequestError('error',raw_data[u'error'])
    if raw_data['status'] == u'exists':
        if raw_data['task']['result'] == 'notfound':
            raise PlayerNotFound()

    #  response seems ok
    result = PlayerUpdateStatus()
    result.queue_position = raw_data['pos']
    result.request_status = raw_data['status']
    result.task_state = raw_data['task']['state']
    return result
        
        

