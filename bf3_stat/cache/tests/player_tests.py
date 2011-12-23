__author__ = 'pengwin4'

import os
from bf3_stat.cache.mongo_wrap import MongoWrapper
from django.test import TestCase
from bf3_stat.cache.player_cache import PlayerCache
from django.utils import simplejson


class PlayerCacheTest(TestCase):

    def setUp(self):
        self.mongo =MongoWrapper(db_name='test')
        path_to_file = 'player_json_test.txt'
        path = os.path.join(os.path.dirname(__file__), path_to_file).replace('\\','/')
        f = open(path,'r')
        str_data = f.read()
        self.data_dict = simplejson.loads(str_data)

    def runTest(self):
        print 'Testing cache.put...'
        self.put_test()
        print 'Testing cache.get...'
        self.get_test()

    def put_test(self):
        cache = PlayerCache(self.mongo.db)
        cache.put('Pengwin88',self.data_dict)
        cache.put('Pengwin88',self.data_dict)

        players =  self.mongo.db['player'].find({'name':'Pengwin88'})
        self.assertEqual(players.count(),1,msg='Duplicated players in db')

        player =  self.mongo.db['player'].find_one({'name':'Pengwin88'})
        self.assertDictEqual(player['data'],self.data_dict)

    def get_test(self):
        cache = PlayerCache(self.mongo.db)
        cache.put('Pengwin88',self.data_dict)

        data = cache.get('Pengwin88')
        self.assertDictEqual(data,self.data_dict)
        
    def tearDown(self):
        print "Destroying MongoDB test database..."
        self.mongo.connection.drop_database('test')
