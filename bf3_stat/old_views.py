# -*- coding: utf-8 -*-
'''
Created on Nov 5, 2011

@author: ivan
'''
import django
import time
from bf3_stat import cache
from bf3_stat.models import Player, MedalData, RibbonData
import simple_file_cache
from django.http import HttpResponse

from django.shortcuts import render_to_response
from django.template import Context
from  django.template import RequestContext

import bf3stat_api

image_url = "http://dl.dropbox.com/u/48383441/images"

def my_render_to_response(request, template, data_dict):
    data_dict['image_url'] = image_url
    return render_to_response(template, data_dict, context_instance=RequestContext(request))

def get_player_data(player_name):
    data_dict, response_status, response_reason = bf3stat_api.request_player_awards(player_name)  # get player data from web
    if response_status != 200:  # if  errors on server occured
        data_dict['status'] == 'request_error'
        return data_dict
    if data_dict['status'] == 'notfound': # if player not found on server
        return data_dict
    return data_dict

def player_not_found_view(request, player_name):
    return my_render_to_response(request, 'player_not_found.html', {'name': player_name})

def player_request_error_view(request, reason):
    return my_render_to_response(request, 'player_request_error.html', {'reason': reason})

def player_awards_view(request, player_name):
    try:
        player = Player.objects.get(name=player_name)
    except Player.DoesNotExist:
        data_dict = get_player_data(player_name)
        if data_dict['status'] == 'request_error':
            return my_render_to_response(request,'player_request_error.html',{})
        if data_dict['status'] == 'notfound':
            return my_render_to_response(request,'player_not_found.html',{'name':player_name})
        if data_dict['stats'] == None:
            return my_render_to_response(request,'player_not_found.html',{'name':player_name})
        player = cache.update_player(data_dict)
    view_dict = {'player':player}
    medals = MedalData.objects.filter(player=player).order_by('-percent')
    view_dict['medals'] = medals
    ribbons = RibbonData.objects.filter(player=player).order_by('-count')
    first_ribbon = ribbons[1]
    view_dict['ribbons'] = ribbons
    return my_render_to_response(request,'player_stats.html',view_dict)


def player_awards_update_view(request, player_name):
    cache.delete_player(player_name)
    data_dict = {'name': player_name}
    return my_render_to_response(request, 'player_update.html', data_dict)


def player_view(request):
    return my_render_to_response(request, 'player.html', {"none": None})

def player_info(request):
    return my_render_to_response(request, 'player_ajax.html', {"none": None})
