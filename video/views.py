from django.shortcuts import render
from .models import Video

def video_list(request):
    videos = Video.objects.all().order_by('-uploaded_at')
    return render(request, 'video/video_list.html', {'videos': videos})
