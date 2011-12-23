__author__ = 'pengwin4'

from django.contrib import admin

from models import Player,MedalData,RibbonData,Medal,Ribbon

admin.site.register(Player)
admin.site.register(MedalData)
admin.site.register(Medal)
admin.site.register(Ribbon)
admin.site.register(RibbonData)