from django.shortcuts import render
from .serializers import *
from .models import *

def test(request):
    if request.method == 'POST':

        post = Brand()
        post.brand_title = request.POST.get('brand_title')
        post.image = request.POST.get('image')
        
        post.save()

        return render(request, 'brand/index.html')

    else:

        return render(request, 'brand/index.html')


def list(request):
    lists = Brand.objects.all()
    args = {'lists': lists}
    return render(request, 'brand/list.html', args)
