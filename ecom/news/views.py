from django.shortcuts import render
from .serializers import *
from .models import *



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
        post.image = request.POST.get('image')
       
        post.save()

        return render(request, 'news_categories/index.html')

    else:

        return render(request, 'news_categories/index.html')


def sub_list(request):
    lists = NewsCategories.objects.all()
    args = {'lists': lists}
    return render(request, 'news_categories/list.html', args)


