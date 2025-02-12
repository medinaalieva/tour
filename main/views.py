from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Image
from video.models import Video
from image2.models import Image2
from itertools import chain


def main_view(request):
    images = Image.objects.all()
    images2 = Image2.objects.all()
    videos = Video.objects.all().order_by('-uploaded_at')

    paginator = Paginator(images, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    paginator2 = Paginator(images2, 8)  # Разбиваем на страницы по 8 элементов
    page_number2 = request.GET.get('page')  # Получаем номер страницы из URL
    page_obj2 = paginator2.get_page(page_number2) 

    media_items = []


    for image in images2:
     media_items.append({'type': 'image', 'file': image.file}) 


    for video in videos:
     media_items.append({'type': 'video', 'file': video.file})
     
    for image in images2:
        image.is_video = False  # Флаг, чтобы знать, что это изображение
        media_items.append(image)

    # Обрабатываем видео
    for video in videos:
        video.is_video = True  # Флаг, чтобы знать, что это видео
        media_items.append(video)


        
  

        media_items2 = list(images2) + list(videos)  # Объединяем изображения и видео
        media_items2 = media_items[:4]  # Ограничиваем до первых 8 элементов





    context = {'media_items': media_items}
    return render(request, 'main/index.html',  {'page_obj': page_obj,  'page_pbj2': page_obj2, 'images2': images2, 'videos': videos , "media_items": media_items} )

