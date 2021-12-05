from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'special_product/index.html')


def sub_list(request):
    # lists = TaxClasses.objects.all()
    # args = {'lists': lists}
    return render(request, 'special_product/list.html')
