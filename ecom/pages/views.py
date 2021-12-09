from django.shortcuts import render, HttpResponseRedirect
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
        post.status = request.POST.get('status')
      
        post.save()

        return render(request, 'Pages/index.html')

    else:

        return render(request, 'Pages/index.html')


def list(request):
    lists = Pages.objects.all()
    args = {'lists': lists}
    return render(request, 'Pages/list.html', args)




def delete_data(request, id):
    if request.method == 'POST':
        pi = Pages.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home/Pages-list')
    

def update_pages(request ,id):
    list = Pages.objects.get(pk=id)
    if request.method =='POST':
        list.page_slug = request.POST.get('page_slug')
        list.page_name_english = request.POST.get('page_name_english')
        list.description_english = request.POST.get('description_english')
        list.page_name_bangla = request.POST.get('page_name_bangla')
        list.description_bangla = request.POST.get('description_bangla')
        list.status = request.POST.get('status')
       
        list.save()
    return render(request, 'pages/edit.html', {'id': id, 'list': list})

