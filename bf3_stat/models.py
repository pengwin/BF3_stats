from django.db import models

class Medal(models.Model):
    """
    Information about Medal entity from bf3stats.com
    """
    medal_id = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    picture = models.URLField()
    needed = models.IntegerField()
    needed_is_hours = models.BooleanField()

    def __unicode__(self):
        return self.name


class Rank(models.Model):
    """
    Information about Player Rank entity from bf3stats.com
    """
    rank_num = models.SmallIntegerField()
    name = models.CharField(max_length=50)
    picture = models.URLField()

    def __unicode__(self):
        return self.name


class Ribbon(models.Model):
    """
    Information about Ribbon entity from bf3stats.com
    """
    ribbon_id = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    picture = models.URLField()

    def __unicode__(self):
        return self.name

class Player(models.Model):
    """
    Information about Player from bf3stats.com
    """
    name = models.CharField(max_length=50)
    rank = models.ForeignKey(Rank)
    last_update = models.DateTimeField()
    medals = models.ManyToManyField(Medal,through='MedalData')
    ribbons = models.ManyToManyField(Ribbon,through='RibbonData')

    def __unicode__(self):
        return self.name

class RibbonData(models.Model):
    """
    Information about Ribbon in player statistics from bf3stats.com
    """
    ribbon = models.ForeignKey(Ribbon)
    player = models.ForeignKey(Player)
    count =  models.IntegerField()

class MedalData(models.Model):
    """
    Information about Medal in player statistics from bf3stats.com
    """
    medal = models.ForeignKey(Medal)
    player = models.ForeignKey(Player)
    count = models.IntegerField()
    progress = models.IntegerField()
    percent = models.IntegerField()

class PlayerUpdateStatus(object):
    """
    Information about Player update request and player update progress from bf3stats.com
    """
    task_state = str()
    request_status = str()
    queue_position = int()
    






