from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.info_album, name='info_album'),
]