"""

"""
__author__ = 'pengwin4'

import datetime

import rank
import medal
import ribbon

from bf3_stat.models import Ribbon, RibbonData, Player, Medal, Rank, MedalData

def update_player(data_dict):
    """
    Updates Player from dict from bf3stats.com
    Creates player if its necessary
    """
    if isinstance(data_dict, dict):

        rank_num = int(data_dict['stats']['rank']['nr'])
        try:
            level = Rank.objects.get(rank_num=rank_num)
        except Rank.DoesNotExist:
            level = rank.create_from_dict(data_dict['stats']['rank'])

        player_name = data_dict['name']
        try:
            player = Player.objects.get(name=player_name)
        except Player.DoesNotExist:
            player = Player()
            player.name = player_name

        player.rank = level
        player.last_update = datetime.datetime.fromtimestamp(data_dict['stats']['date_update'])

        player.save()

        for key in data_dict['stats']['medals'].keys():
            medal.update_from_dict(player,data_dict['stats']['medals'],key)

        for key in data_dict['stats']['ribbons'].keys():
            ribbon.update_from_dict(player,data_dict['stats']['ribbons'],key)

        return player
    #TODO: TypeError exception or something simmilar
  