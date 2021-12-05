from django.shortcuts import render, HttpResponseRedirect
from .serializers import *
from .models import *
from django.core.files.storage import FileSystemStorage



def test(request):
    if request.method == 'POST':

        post = Manufacturer()
        # table coulumn name = form input name
        post.name = request.POST.get('name')
        post.manufacturer_url = request.POST.get('manufacturers_url')
        
        image = request.FILES['image']
        fss = FileSystemStorage()
        file_image = fss.save(image.name, image)
        file_image_url = fss.url(file_image)
        post.image = file_image_url
       
        post.save()
        

        return render(request, 'manufacturer/index.html')

    else:

        return render(request, 'manufacturer/index.html')


def list(request):
    lists = Manufacturer.objects.all()
    args = {'lists': lists}
    return render(request, 'manufacturer/list.html', args)


def delete_data(request, id):
    if request.method == 'POST':
        pi = Manufacturer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home/manufacturer-list')

