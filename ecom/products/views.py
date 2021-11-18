from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'products/index.html')


def list(request):
    # lists = products.objects.all()
    # args = {'lists': lists}
    return render(request, 'products/list.html', )

def sub_test(request):
    return render(request, 'product_attributes/index.html')

def attribute_list(request):
    return render(request, 'products_attributes/list.html', )


