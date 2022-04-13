from django.template import loader
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Track, Album, Artist

# Create your views here.

def index(request):
    album_list = Album.objects.order_by('title')[:]
    template = loader.get_template('disks/index.html')
    context = {
        'album_list': album_list,
    }
    return HttpResponse(template.render(context, request))

def info_album(request, album_id):
    try:
        album= Album.objects.get(pk=album_id)
        track_list = Track.objects.filter(album=album).all()
    except Album.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'disks/info_album.html', {'album': album, 'track_list' : track_list})
