from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def category(request):
    return render(request, 'category/index.html')

def profile(request):
    return render(request, 'profile/index.html')