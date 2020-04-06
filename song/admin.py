from django.contrib import admin
from .models import Song, SongGroup, SongList
# Register your models here.


class SongAdmin(admin.ModelAdmin):
    list_display = ["name", "create_time", "user"]


admin.site.register(Song, SongAdmin)


class SongListAdmin(admin.ModelAdmin):
    list_display=["user", "song", "create_time", "sang_time", "sponsor", "money", "is_sang"]


admin.site.register(SongList,SongListAdmin )
