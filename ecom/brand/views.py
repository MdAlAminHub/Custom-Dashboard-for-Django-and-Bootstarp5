from django.shortcuts import render ,HttpResponseRedirect

from .serializers import *
from .models import *
from django.core.files.storage import FileSystemStorage

def test(request):
    if request.method == 'POST':

        post = Brand()
        post.brand_title = request.POST.get('brand_title')
        # post.image = request.POST.get('image')
        image = request.FILES['image']
        fss = FileSystemStorage()
        file_image = fss.save(image.name, image)
        file_image_url = fss.url(file_image)
        post.image = file_image_url
        post.save()

        return render(request, 'brand/index.html')

    else:

        return render(request, 'brand/index.html')


def list(request):
    lists = Brand.objects.all()
    args = {'lists': lists}
    return render(request, 'brand/list.html', args)


def delete_data(request, id):
    if request.method == 'POST':
        pi = Brand.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home/brand-list')



  


