from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .models import *


def test(request):
    if request.method == 'POST':

        post = Categories()
        post.name_bangla = request.POST.get('name_bangla')
        post.name_english = request.POST.get('name_english')
        post.icon = request.POST.get('image')
        post.icon = request.POST.get('icon')
        post.save()

        return render(request, 'categories/index.html')

    else:

        return render(request, 'categories/index.html')


def list(request):
    lists = Categories.objects.all()
    args = {'lists': lists}
    return render(request, 'categories/list.html', args)


def delete_data(request, id):
    if request.method == 'POST':
        pi = Categories.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/home/category-list')
    
    
    
def sub_test(request):
    if request.method == 'POST':

        post = SubCategories()
        post.name = request.POST.get('name_bangla')
        post.code = request.POST.get('name_english')
        post.icon = request.POST.get('image')
        post.icon = request.POST.get('icon')
        post.save()

        return render(request, 'sub_categories/index.html')

    else:

        return render(request, 'sub_categories/index.html')


def sub_list(request):
    lists = SubCategories.objects.all()
    args = {'lists': lists}
    return render(request, 'sub_categories/list.html', args)


