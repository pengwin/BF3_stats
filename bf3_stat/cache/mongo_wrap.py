__author__ = 'pengwin4'


import pymongo

class MongoWrapper(object):
    """
    Simple wrapper for MongoDB
    """

    DB_NAME = 'bf3stats'
    DB_IP = "127.0.0.1"
    DB_PORT = 27017

    db = property(fget=lambda self: self._db)
    connection = property(fget=lambda self: self._connection)

    def __init__(self,db_ip=DB_IP,db_port=DB_PORT,db_name=DB_NAME):
         self._connection = pymongo.Connection(db_ip,db_port)
         self._db = self._connection[db_name]


  