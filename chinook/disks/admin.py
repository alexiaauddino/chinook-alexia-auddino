from django.contrib import admin

from .models import Album, Artist, Track

# Register your models here.

class TrackAdmin(admin.ModelAdmin):
    search_fields = ['name','album__title']
    list_display = ('name', 'composer', 'album','unitPrice')
    

class AlbumAdmin(admin.ModelAdmin):
    search_fields = ['title','artist__name']
    list_display = ('title', 'artist')

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Track, TrackAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
