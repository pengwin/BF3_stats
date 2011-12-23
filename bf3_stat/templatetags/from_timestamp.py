__author__ = 'pengwin4'

import datetime

from django import template
register = template.Library()

@register.filter(name='timestamp')
def _convert_dates_from_timestamps(timestamp):
    """
    Converts  from unix timestamp to date_time
    returns date_time
    """
    return datetime.datetime.fromtimestamp(timestamp)
  