from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'orders/index.html')
