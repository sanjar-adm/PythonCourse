from django.shortcuts import render
from .models import Employer

def index(request):
    data = Employer.objects.all()
    context = {
        'data' : data
    }
    return render(request,
                  template_name='index.html',
                  context=context)
