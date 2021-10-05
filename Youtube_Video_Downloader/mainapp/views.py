from django.shortcuts import render
from pytube import YouTube

# Create your views here.

def index(request):
    if request.method == 'POST' and request.POST:
     urls = request.POST["youtubeurl"]
     url = str(urls)
     youtubeOBJ = YouTube(url)
     video = youtubeOBJ.streams.first()
     video.download()
     return render(request,'mainapp/index.html')
    else:
     return render(request,'mainapp/index.html')


    