from django.shortcuts import render
from .serializers import *
from .models import *


def test(request):
    if request.method == 'POST':

        post = Pages()
        post.page_slug = request.POST.get('page_slug')
        post.page_name_english = request.POST.get('page_name_english')
        post.description_english = request.POST.get('description_english')
        post.page_name_bangla = request.POST.get('page_name_bangla')
        post.description_bangla = request.POST.get('description_bangla')
      
        post.save()

        return render(request, 'Pages/index.html')

    else:

        return render(request, 'Pages/index.html')


def list(request):
    lists = Pages.objects.all()
    args = {'lists': lists}
    return render(request, 'Pages/list.html', args)
