from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def music_home(request):
    return HttpResponse("<h1>Music apps</h1>")

def song_list(request):
    songs=["song1","song2","song3","song4","song5","song6","song7"]
    output=""
    for song in songs:
        output+=song+"<br>"
    return HttpResponse("<h1>This is a list of songs</h1><br>"+output)