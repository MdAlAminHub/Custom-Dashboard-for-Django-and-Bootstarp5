from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'countries/index.html')


def sub_test(request):
    return render(request, 'tax_classes/index.html')


def tax_rates(request):
    return render(request, 'tax_rates/index.html')


def zones(request):
    return render(request, 'zones/index.html')


# def rahim(request):
#     return render(request, 'zones/index.html')


# def test(request):
#     return render(request, 'sub_categories/index.html')
