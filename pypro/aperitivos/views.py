from django.shortcuts import render

# Create your views here.


def video(request, slug):
    video = {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 576473838}
    return render(request, 'aperitivos/video.html', context={'video': video})


