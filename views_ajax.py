__author__ = 'pengwin4'

from django.http import HttpResponse
from django.utils import simplejson

from bf3_stat.models import Player

# Views available via ajax requests

images_url = "http://dl.dropbox.com/u/48383441/images"

class json(object):
    def __init__(self,function):
        self.f = function

    def __call__(self, *args):
        response = self.f(*args)
        return HttpResponse(simplejson.dumps(response),mimetype='application/javascript')

@json
def player_ajax_test(request):
    data_dict= {'her':'her'}
    if request.is_ajax():
        data_dict = {'img':images_url+'/bf3/servicestars/servicestar.png'}
    return data_dict

@json
def player_search(request,player_name_part):
    data_dict= {}
    if len(player_name_part) > 2:
        players = Player.objects.filter(name__startswith=player_name_part)
        for player in players:
            data_dict[player.name] = {'rank':player.rank.rank_num,'rank_img':player.rank.picture}
    return data_dict

        