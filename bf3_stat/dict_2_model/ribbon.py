"""
Provides link between Ribbon and RibbonData data and data dict
"""
__author__ = 'pengwin4'

from bf3_stat.models import Ribbon,RibbonData

def create_from_dict(ribbons_dict, ribbon_id):
    """
    Creates Ribbon from bf3stats dict
    """
    if isinstance(ribbons_dict, dict):
        ribbon = Ribbon()
        ribbon.ribbon_id = ribbon_id
        ribbon.name = ribbons_dict[ribbon_id]['name']
        ribbon.description = ribbons_dict[ribbon_id]['desc']
        ribbon.picture  = "/awards_m/{ribbon_id}.png".format(ribbon_id=ribbon_id)
        ribbon.save()
        return ribbon
    #TODO: TypeError exception or something simmilar


def update_from_dict(player,ribbons_dict, ribbon_id):
    """
    Updates RibbonData from data dict from bf3stats.com
    Creates Ribbon if it is necessary
    """
    if isinstance(ribbons_dict, dict):
        try:
            ribbon = Ribbon.objects.get(ribbon_id=ribbon_id)
        except Ribbon.DoesNotExist:
            ribbon = create_from_dict(ribbons_dict,ribbon_id)

        try:
            ribbon_data = RibbonData.objects.get(ribbon=ribbon,player=player)
        except RibbonData.DoesNotExist:
            ribbon_data = RibbonData()
            ribbon_data.player = player
            ribbon_data.ribbon = ribbon

        ribbon_data.count = ribbon.count = int(ribbons_dict[ribbon_id]['count'])
        ribbon_data.save()
    #TODO: TypeError exception or something simmilar
  