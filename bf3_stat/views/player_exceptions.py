__author__ = 'pengwin4'

class PlayerNotFound(Exception):
    '''
    Exception raises when player not found in bf3stat.com database
    '''
    pass


class PlayerRequestError(Exception):
    """
    Exception raises when bf3stats response is different from 200
    """
    def __init__(self, response_status, response_reason):
        self.message = "Request error \'{0}\' reason \'{1}\'".format(response_status, response_reason)
  