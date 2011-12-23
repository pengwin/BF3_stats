"""
Provides link bentween Medal and Medal data and data dict
"""
__author__ = 'pengwin4'

from bf3_stat.models import Medal,MedalData

def create_from_dict(medals_dict, medal_id):
    """
    Creates Medal from data dict from bf3stats.com
    """
    if isinstance(medals_dict, dict):
        medal = Medal()
        medal.medal_id = medal_id
        medal.name = medals_dict[medal_id]['name']
        medal.description = medals_dict[medal_id]['desc']
        medal.picture = "/awards_m/{medal_id}.png".format(medal_id=medal_id)

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


def update_from_dict(player,medals_dict, medal_id):
    """
    Updates MedalData from data dict from bf3stats.com
    Creates Medal if it is necessary
    """
    if isinstance(medals_dict, dict):
        try:
            medal = Medal.objects.get(medal_id=medal_id)
        except Medal.DoesNotExist:
            medal = create_from_dict(medals_dict, medal_id)

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

  