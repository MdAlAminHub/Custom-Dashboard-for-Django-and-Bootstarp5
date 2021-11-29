from django.shortcuts import render
from .serializers import *
from .models import *
from django.core.files.storage import FileSystemStorage



def test(request):
    if request.method == 'POST':

        post = Manufacturer()
        post.name = request.POST.get('name')
        post.manufacturer_url = request.POST.get('manufacturer_url ')
       
        image = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(image.name, image)
        file_url = fss.url(file)
        post.image = file_url
       
        post.save()
        print('-----Worked!-----')

        return render(request, 'manufacturer/index.html')

    else:

        return render(request, 'manufacturer/index.html')


def list(request):
    lists = Manufacturer.objects.all()
    args = {'lists': lists}
    return render(request, 'manufacturer/list.html', args)

