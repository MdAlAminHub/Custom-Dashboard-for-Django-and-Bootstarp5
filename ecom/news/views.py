from django.shortcuts import render
from .serializers import *
from .models import *
from django.core.files.storage import FileSystemStorage



def test(request):
    return render(request, 'news/index.html')


def list(request):
    lists = News.objects.all()
    args = {'lists': lists}
    return render(request, 'news/list.html', args)


def sub_test(request):
    if request.method == 'POST':

        post = NewsCategories()
        post.name_english = request.POST.get('name_english')
        post.name_bangla = request.POST.get('name_bangla')
        
        image = request.FILES['image']
        fss = FileSystemStorage()
        file_image = fss.save(image.name, image)
        file_image_url = fss.url(file_image)
        post.image = file_image_url
        
        post.created = request.POST.get('created')
        post.updated = request.POST.get('updated')
       
        post.save()

        return render(request, 'news_categories/index.html')

    else:

        return render(request, 'news_categories/index.html')


def sub_list(request):
    lists = NewsCategories.objects.all()
    args = {'lists': lists}
    return render(request, 'news_categories/list.html', args)


