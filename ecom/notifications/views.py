from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'devices/index.html')


def sub_test(request):
    return render(request, 'send_notifications/index.html')
