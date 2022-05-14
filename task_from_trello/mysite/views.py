from django.shortcuts import redirect, render
from .models import *
from .forms import *

def index(request):
    posts = Contact.objects.all()
    search_person = request.GET.get('query')
    result_of_search = Contact.objects.filter(first_name=search_person)
    context = {'posts': posts, 'result_of_search': result_of_search}
    return render(request, template_name='index.html', context=context)


def blank(request):
    return render(request, template_name='blank.html')


def add_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('form')
    else:
        form = ContactForm()
    return render(request,
                  'form.html',
                  context={'form': form})