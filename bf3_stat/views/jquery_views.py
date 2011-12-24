"""
Views for jquery page version
"""
__author__ = 'pengwin4'

from context_stuff import my_render_to_response
from player_exceptions import PlayerNotFound,PlayerRequestError
import get_player_dict
import update_player
import settings

from bf3_stat.models import Player,MedalData,RibbonData,PlayerUpdateStatus

def index_view(request):
    return my_render_to_response(request,'jquery/player.html')

def player_awards_view(request,player_name):
    try:
        player = get_player_dict.get_player(player_name)
    except PlayerNotFound:
        #return my_render_to_response(request,'jquery/player_not_found.html',{ 'name': player_name})
        return player_update_view(request,player_name)
    except PlayerRequestError as ex:
        response_dict = {}
        if settings.DEBUG:
            response_dict['error'] = ex.message
        return my_render_to_response(request,'jquery/player_request_error.html',response_dict)

    medals = MedalData.objects.filter(player=player).order_by('-percent')
    ribbons = RibbonData.objects.filter(player=player).order_by('-count')
    player_dict = {'player' : player,'ribbons' : ribbons, 'medals' : medals}

    return my_render_to_response(request,'jquery/player_stats.html',player_dict)

def player_update_view(request,player_name):
    # delete player if exists
    try:
        player = Player.objects.get(name=player_name) # gets from db first
        player.delete()
    except Player.DoesNotExist:
        pass

    # update player status on server
    try:
        update_status = update_player.update_player(player_name)
    except PlayerNotFound:
        return my_render_to_response(request,'jquery/player_not_found.html',{ 'name': player_name})
    except PlayerRequestError as ex:
        response_dict = {}
        if settings.DEBUG:
            response_dict['error'] = ex.message
        return my_render_to_response(request,'jquery/player_request_error.html',response_dict)
	
    if update_status.task_state == u'finished':
	return player_awards_view(request,player_name)
    return my_render_to_response(request,'jquery/player_update.html',{'update_status' : update_status})


    
        










