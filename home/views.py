from django.shortcuts import render
from django.views.generic.base import TemplateView

def home(request):
    return render(request, 'home/home.html', {})

def login(request):
    return render(request, 'home/login.html',{})

class IndexView(TemplateView): # TemplateView를 상속 받는다.
    template_name = 'home/login.html'