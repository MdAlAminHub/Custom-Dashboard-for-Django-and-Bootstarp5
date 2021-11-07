from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'packages/index.html')


def sub_test(request):
    return render(request, 'packages_type/index.html')


def sub_type_test(request):
    return render(request, 'packages_type_attribute/index.html')


# def test(request):
#     return render(request, 'sub_categories/index.html')
