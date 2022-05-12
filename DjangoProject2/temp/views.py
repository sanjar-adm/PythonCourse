import imp
from django.shortcuts import render
from .models import Images

def index(request):
    data = Images.objects.all()
    context = {
        'data' : data
    }
    return render(request,
                  template_name='index.html', context=context)

def about(request):
    return render(request,
                  template_name='about.html')

def contact(request):
    return render(request,
                  template_name='contact.html')

def videos(request):
    data = Images.objects.all()
    context = {'data' : data}
    return render(request,
                  template_name='videos.html', context=context)

def photo_detail(request, id_):
    data = Images.objects.get(id=id_)
    all_data = Images.objects.all()
    context = {'data' : data, 'all_data': all_data}
    return render(request,
                  template_name='photo-detail.html', context=context)

def video_detail(request):
    data = Images.objects.all()
    context = {
        'data' : data
    }
    return render(request,
                template_name='video-detail.html', context=context)
