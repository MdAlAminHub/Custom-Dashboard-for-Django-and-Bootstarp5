from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'order_status/index.html')


def sub_test(request):
    return render(request, 'settings/index.html')
