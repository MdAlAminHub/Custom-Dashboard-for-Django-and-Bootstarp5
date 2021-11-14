from django.shortcuts import render
from .serializers import *
from .models import *


def test(request):
    if request.method == 'POST':
        post = Manufacturer()
        post.name= request.POST.get('name')
        post.manufacturer_url = request.POST.get('manufacturer_url')
        post.image = request.POST.get('image')
        post.save()
        return render(request, 'manufacturer/index.html')
    else:
        return render(request, 'manufacturer/index.html')


def list(request):
    lists = Manufacturer.objects.all()
    args = {'lists': lists}
    return render(request, 'manufacturer/list.html', args)
