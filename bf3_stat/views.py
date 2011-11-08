# -*- coding: utf-8 -*-
'''
Created on Nov 5, 2011

@author: ivan
'''
import django
import datetime
import httplib, urllib
import simple_file_cache
from django.http import HttpResponse

from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import Context
from  django.template import RequestContext


image_url = "http://dl.dropbox.com/u/48383441/images"

def my_render_to_response(request,template,data_dict):
	data_dict['image_url'] = image_url
    	return render_to_response(template,data_dict,context_instance = RequestContext(request))
    
'''
gets json response from api.bf3stats.com
returns tuple (data dictionary, response status, response reason)
'''
def request_player_awards(player_name):
    opts = "clear,awards,rank,scores,awardsInfo"
    params = urllib.urlencode({'opt': opts, 'player': player_name})
    headers = {'Content-type': "application/x-www-form-urlencoded",'User-Agent': "BF3StatsAPI/0.1" }
    url = "/{platform}/{data_group}/".format(platform = "pc",data_group="player")
    conn = httplib.HTTPConnection("api.bf3stats.com")
    conn.request("POST", url, params, headers)
    response = conn.getresponse()
    raw_data = response.read()
    conn.close()
    data_dict = simplejson.loads(raw_data)
    return (data_dict,response.status, response.reason,)

 
def player_not_found_view(request,player_name):
    return my_render_to_response(request,'player_not_found.html',{'name':player_name})


def player_request_error_view(request,reason):
    return my_render_to_response(request,'player_request_error.html',{'reason':reason})

def get_medals(data_dict):
    medals = []
    for medal in data_dict['stats']['medals'].keys():
        medal_id = medal
        medal_name = data_dict['stats']['medals'][medal]['name']
        medal_description = data_dict['stats']['medals'][medal]['desc']
        medal_count = int(data_dict['stats']['medals'][medal]['count'])
        medal_needed = float(data_dict['stats']['medals'][medal]['needed'])
	medal_needed = medal_needed/(medal_count +1)
        goal_in_minutes = medal_needed > 1000 # medal goal is minutes
        if goal_in_minutes:
            medal_needed = medal_needed/3600.0 # convert to hours
        medal_progress = float(data_dict['stats']['medals'][medal]['curr'])
        if goal_in_minutes:
            medal_progress = medal_progress/3600.0 # convert to hours            
        medal_progress = medal_progress - medal_count*medal_needed
        medal_progress_percent = (medal_progress/medal_needed)*100
        medal_dict = {'id': medal_id,'name' : medal_name,'description' : medal_description,'count':medal_count,\
                      'progress' : int(medal_progress),'needed' : int(medal_needed),'percent': int(medal_progress_percent)}
        medals.append(medal_dict)
    return medals

def group_array_by(buffer,group_size):
    temp = buffer
    grouped = []
    while len(temp) >= group_size: # grouping
        grouped.append(temp[0:5])
        del temp[0:5]
    if len(temp) > 0:
        grouped.append(temp)
    return grouped

def get_ribbons(data_dict):
    ribbons = []
    for ribbon in data_dict['stats']['ribbons'].keys():
        ribbon_id = ribbon
        ribbon_name = data_dict['stats']['ribbons'][ribbon]['name']
        ribbon_description = data_dict['stats']['ribbons'][ribbon]['desc']
        ribbon_count = data_dict['stats']['ribbons'][ribbon]['count']      
        ribbon_dict = {'id': ribbon_id,'name' : ribbon_name,'description' : ribbon_description,'count':ribbon_count}
        ribbons.append(ribbon_dict)
    return ribbons


def player_awards_data_view(request,data_dict):
    last_update = datetime.date.fromtimestamp(data_dict['stats']['date_update'])
    rank = data_dict['stats']['rank']['nr'] 
                                                       
    medals = get_medals(data_dict)
    medals = sorted(medals,key=lambda x: x['percent']) # sorting by completion
    medals.reverse()
    medals_5th = group_array_by(medals,5) #medals grouped by 5th
    
    ribbons = get_ribbons(data_dict)
    ribbons = sorted(ribbons,key=lambda x: x['count']);
    ribbons.reverse()
    ribbons_5th = group_array_by(ribbons,5)    
        
    result_dict =  {'name':data_dict['name'],'rank':rank,'last_update':last_update,'medals_5th' : medals_5th,'ribbons_5th' : ribbons_5th}
    return my_render_to_response(request,'player_stats.html',result_dict)
    

def player_awards_view(request,player_name):  
    if simple_file_cache.if_exists(player_name): # search player data in cache
        data_dict = simple_file_cache.get(player_name)
        return player_awards_data_view(request,data_dict)
    #player data not found in cache
    data_dict,response_status,response_reason = request_player_awards(player_name) # get player data from web       
    if response_status != 200:  # if some errors occured
        return player_request_error_view(request,response_reason)
    if data_dict['status'] == 'notfound': # if player not found on server
        return player_not_found_view(request,player_name)
    #everything is ok
    simple_file_cache.put(player_name,data_dict) # save player data
    return player_awards_data_view(request,data_dict)

def player_awards_update_view(request,player_name):  
    simple_file_cache.delete(player_name)
    data_dict = {'name':player_name}
    return my_render_to_response(request,'player_update.html',data_dict)

    
def player_view(request):
    return my_render_to_response(request,'player.html',{"none":None})
