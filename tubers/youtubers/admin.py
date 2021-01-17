from django.contrib import admin
from .models import YouTuber
# Register your models here.


class YtAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subs_count', 'is_featured']
    search_fields = ['camera', 'category']
    list_display_links = ['id']


admin.site.register(YouTuber, YtAdmin)
