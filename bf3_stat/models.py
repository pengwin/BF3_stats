from django.db import models


class Medal(models.Model):
    medal_id = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    picture = models.URLField()
    needed = models.IntegerField()
    needed_is_hours = models.BooleanField()
    
    def __unicode__(self):
        return self.name


class Rank(models.Model):
    rank_id = models.CharField(max_length=5)
    rank_num = models.SmallIntegerField()
    name = models.CharField(max_length=50)
    picture = models.URLField()

    def __unicode__(self):
        return self.name


class Ribbon(models.Model):
    ribbon_id = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    picture = models.URLField()

    def __unicode__(self):
        return self.name


class RibbonData(models.Model):
    ribbon = models.ForeignKey(Ribbon)
    count = models.IntegerField()

    def __unicode__(self):
        return self.name


class MedalData(models.Model):
    medal = models.ForeignKey(Medal)
    count = models.IntegerField()
    progress = models.FloatField()
    percent = models.IntegerField()

class PlayerData(models.Model):
    name = models.CharField(max_length=50)
    rank = models.ForeignKey(Rank)
    last_update = models.DateTimeField()
    medals = models.ManyToManyField(MedalData)
    ribbons = models.ManyToManyField(RibbonData)

    def __unicode__(self):
        return self.name




