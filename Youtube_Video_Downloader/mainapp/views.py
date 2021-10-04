from django.shortcuts import render
import pytube;

# Create your views here.

def index(request):
    url = "https://www.youtube.com/watch?v=t40o7ml-8Ng&list=LL&index=5&ab_channel=101Barz";
    youtube = pytube.Youtube(url)
    video = youtube.streams.first()
    video.download()
    stringobj = "teststring"
    return render(request,'mainapp/index.html', {'stringobj':stringobj})