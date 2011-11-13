
from django.test import TestCase
import datetime
import os
from models import Rank
from models import Player

import dict_converter
from django.utils import simplejson

class DictConvertTest(TestCase):
    
    def test_player_update(self):
        path_to_file = 'player_json_test.txt'
        path = os.path.join(os.path.dirname(__file__), path_to_file).replace('\\','/')
        f = open(path,'r')
        str_data = f.read()
        data_dict = simplejson.loads(str_data)

        dict_converter.update_player(data_dict)

        #creation test
        player = Player.objects.get(name='Pengwin88')
        self.assertEqual(player.rank.rank_num,19)

        id = player.id

        data_dict['stats']['rank']['nr'] = '25'
        dict_converter.update_player(data_dict)

        #update test
        player = Player.objects.get(name='Pengwin88')
        self.assertEqual(player.id,id)
        self.assertEqual(player.rank.rank_num,25)


