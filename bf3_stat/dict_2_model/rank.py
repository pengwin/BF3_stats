"""
Provides link between Rank data and data dict
"""
__author__ = 'pengwin4'

from bf3_stat.models import Rank

def create_from_dict(rank_dict):
    """
    Creates Rank from dict from bf3stast.com
    """
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
        rank.picture = "/rankslarge/{rank_pref}{rank_id}.png".format(rank_pref = rank_pref,rank_id=rank_id)
        rank.save()
        return rank
    #TODO: TypeError exception or something simmilar
  