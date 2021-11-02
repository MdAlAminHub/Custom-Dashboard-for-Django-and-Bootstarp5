from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'flash_deal_product/index.html')
