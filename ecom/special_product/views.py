from django.shortcuts import render
from .models import *


def test(request):
    if request.method == 'POST':

        post = Special_Product()
        post.products = request.POST.get('products')
        post.status = request.POST.get('status')
       
        
        post.save()

    return render(request, 'special_product/index.html')


def sub_list(request):
    lists = Special_Product.objects.all()
    args = {'lists': lists}
   
    return render(request, 'special_product/list.html', args)
