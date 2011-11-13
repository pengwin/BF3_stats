import datetime
from multiprocessing.dummy import dict #TODO: delete
from bf3_stat.models import Ribbon, RibbonData, Player, Medal, Rank, MedalData

image_url = "http://dl.dropbox.com/u/48383441/images/bf3"

def create_medal_from_dict(medals_dict, medal_id):
    if isinstance(medals_dict, dict):
        medal = Medal()
        medal.medal_id = medal_id
        medal.name = medals_dict[medal_id]['name']
        medal.description = medals_dict[medal_id]['desc']
        medal.picture = "{image_url}/awards_m/{medal_id}.png".format(image_url=image_url, medal_id=medal_id)

        medal_needed = float(medals_dict[medal_id]['needed'])
        medal_count = int(medals_dict[medal_id]['count'])
        medal_needed /= (medal_count + 1)
        goal_in_minutes = medal_needed > 1000 # medal goal is minutes
        if goal_in_minutes:
            medal_needed /= 3600.0 # convert to hours
        medal.needed = int(medal_needed)
        medal.needed_is_hours = goal_in_minutes
        medal.save()
        return medal
    #TODO: TypeError exception or something simmilar


def update_medal_data(player,medals_dict, medal_id):
    if isinstance(medals_dict, dict):
        try:
            medal = Medal.objects.get(medal_id=medal_id)
        except Medal.DoesNotExist:
            medal = create_medal_from_dict(medals_dict, medal_id)
            
        try:
            medal_data = MedalData.objects.get(medal=medal,player=player)
        except MedalData.DoesNotExist:
           medal_data = MedalData()
           medal_data.medal = medal
           medal_data.player = player
        
        medal_data.count = int(medals_dict[medal_id]['count'])
        medal_progress = float(medals_dict[medal_id]['curr'])
        if medal.needed_is_hours:
            medal_progress  /= 3600.0 # convert to hours
        medal_progress  = medal_progress  - medal_data.count * medal.needed
        medal_percent = (medal_progress / medal.needed) * 100
        
        medal_data.progress = int(medal_progress)
        medal_data.percent = int(medal_percent)
        medal_data.save()
    #TODO: TypeError exception or something simmilar


def create_ribbon_from_dict(ribbons_dict, ribbon_id):
    if isinstance(ribbons_dict, dict):
        ribbon = Ribbon()
        ribbon.ribbon_id = ribbon_id
        ribbon.name = ribbons_dict[ribbon_id]['name']
        ribbon.description = ribbons_dict[ribbon_id]['desc']
        ribbon.save()
        return ribbon
    #TODO: TypeError exception or something simmilar


def update_ribbon_data(player,ribbons_dict, ribbon_id):
    if isinstance(ribbons_dict, dict):
        try:
            ribbon = Ribbon.objects.get(ribbon_id=ribbon_id)
        except Ribbon.DoesNotExist:
            ribbon = create_ribbon_from_dict(ribbons_dict,ribbon_id)

        try:
            ribbon_data = RibbonData.objects.get(ribbon=ribbon,player=player)
        except RibbonData.DoesNotExist:
            ribbon_data = RibbonData()
            ribbon_data.player = player
            ribbon_data.ribbon = ribbon
            
        ribbon_data.count = ribbon.count = int(ribbons_dict[ribbon_id]['count'])
        ribbon_data.save()
    #TODO: TypeError exception or something simmilar


def create_rank_from_dict(rank_dict):
    if isinstance(rank_dict, dict):
        rank = Rank()
        rank.rank_num = int(rank_dict['nr'])
        rank.name = rank_dict['name']
        if rank.rank_num > 45:
            rank_pref = 'ss'
            rank_id = rank.rank_num - 45
        else:
            rank_pref = 'r'
            rank_id = rank.rank_num
        rank.picture = "{image_url}/rankslarge/{rank_pref}{rank_id}.png".format(image_url=image_url, rank_pref = rank_pref,rank_id=rank_id)
        rank.save()
        return rank
    #TODO: TypeError exception or something simmilar


def update_player(data_dict):
    if isinstance(data_dict, dict):

        rank_num = int(data_dict['stats']['rank']['nr'])
        try:
            rank = Rank.objects.get(rank_num=rank_num)
        except Rank.DoesNotExist:
            rank = create_rank_from_dict(data_dict['stats']['rank'])

        player_name = data_dict['name']
        try:
            player = Player.objects.get(name=player_name)
        except Player.DoesNotExist:
            player = Player()
            player.name = player_name
            
        player.rank = rank
        player.last_update = datetime.date.fromtimestamp(data_dict['stats']['date_update'])

        player.save()

        for medal in data_dict['stats']['medals'].keys():
            update_medal_data(player,data_dict['stats']['medals'],medal)

        for ribbon in data_dict['stats']['ribbons'].keys():
            update_ribbon_data(player,data_dict['stats']['ribbons'],ribbon)
            
    #TODO: TypeError exception or something simmilar



        


        

        