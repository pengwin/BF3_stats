__author__ = 'pengwin4'

from django.test import TestCase
from bf3_stat import bf3stat_api


class PlayerRequestsTest(TestCase):

    def test_request_player_update(self):
        raw_data,status,response = bf3stat_api.signed_request_player_update('Pengwin88')
        print raw_data
        self.assertEqual(status,200)
        self.assertEqual(raw_data['status'],'added')

  