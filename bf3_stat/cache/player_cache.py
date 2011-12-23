"""
Simple cache for json response from bf3stats server
Uses MongoDB
"""
__author__ = 'pengwin4'

import pymongo

class PlayerCache(object):
    """
    Simple player data cache
    Works with MongoDB database
    """
    _collection = None

    def __init__(self, mongodb):
        self._collection = mongodb['player']

    def _get_player(self, player_name):
        """ Gets player data from db
         Args:
            player_name: no comments
        Returns:
            Dict from db or None if no player with this name
        """
        return self._collection.find_one({'name': player_name})

    def put(self, player_name, data):
        """ Puts player dict into cache
        Save or update player's data
        Args:
            player_name: no comments
            data: dict with json response
        Returns:
            None
        """
        if isinstance(data, dict):
            player = self._get_player(player_name)
            if player == None:
                player = {'name': player_name}
            player['data'] = data
            self._collection.insert(player)
            #TODO: TypeError exception or something simmilar

    def get(self, player_name):
        """ Gets player data from cache
         Args:
            player_name: no comments
        Returns:
            Dict with json reponse or None if no player with this name
        """
        player = self._get_player(player_name)
        return player['data'''] if player else None





  