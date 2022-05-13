from django.shortcuts import redirect, render
from .models import *
from .forms import ContactForm


def index(request):
    post = Image.objects.all()
    context = {'post' : post}
    return render(request,
                  template_name='index.html', context=context)


def about(request):
    return render(request, template_name='about.html')


def videos(request):
    posts = Video.objects.all()
    context = {'posts' : posts}
    return render(request,
                  template_name='videos.html', context=context)


def photo_detail(request, id_):
    post = Image.objects.get(id=id_)
    posts = Image.objects.all()
    context = {'post': post, 'posts': posts}
    return render(request,
                  template_name='photo-detail.html', context=context)


def video_detail(request, id_):
    post = Video.objects.get(id=id_)
    posts = Video.objects.all()
    context = {'post': post, 'posts': posts}
    return render(request,
                template_name='video-detail.html', context=context)


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  context={'form': form})
