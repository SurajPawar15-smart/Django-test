from django.urls import path
from . import views
urlpatterns = [

    path('',views.music_home,name='music_home'),
    path('song_list',views.song_list,name='song_list')
]
