
from django.test import TestCase
import datetime
from bf3_stat import bf3stat_api

from django.utils import simplejson

class BF3StatAPITest(TestCase):

    def test_request_player_update(self):
        raw_data = bf3stat_api.signed_request_player_update('DimbaZ')
        print raw_data

  