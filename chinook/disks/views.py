from turtle import title
from django.template import loader
from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import Track, Album

# Create your views here.

def index(request):
    template = loader.get_template('disks/index.html')
    if request.method == 'GET': # If the form is submitted
        search = request.GET.get('search', None)
        album_list = Album.objects.order_by('title')[:]
        track_list = Track.objects.order_by('name')[:]
        context = {
            'album_list': album_list,
            'track_list': track_list,
            'search' : search,
        }
    else:
        album_list = Album.objects.order_by('title')[:]
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
