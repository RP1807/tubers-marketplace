from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img width="40" src="{}" />'.format(object.photo.url))

    list_display = ['id', 'first_name', 'last_name', 'myphoto', 'role', 'created_at']
    list_display_links = ['id']


# Register your models here.
admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)

