from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'categories/index.html')


def test(request):
    return render(request, 'sub_categories/index.html')
