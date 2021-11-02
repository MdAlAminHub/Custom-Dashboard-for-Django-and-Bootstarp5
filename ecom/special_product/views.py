from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'special_product/index.html')
