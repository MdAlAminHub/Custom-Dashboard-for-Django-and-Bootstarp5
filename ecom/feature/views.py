from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'create_feature/index.html')


def sub_test(request):
    return render(request, 'manage_feature/index.html')
