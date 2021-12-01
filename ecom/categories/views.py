from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.core.files.storage import FileSystemStorage


def test(request):
    if request.method == 'POST':

        post = Categories()
        post.name_bangla = request.POST.get('name_bangla')
        post.name_english = request.POST.get('name_english')
        
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        post.image = file_url
        
        icon = request.FILES['icon']
        fss = FileSystemStorage()
        file_icon = fss.save(icon.name, icon)
        file_icon_url = fss.url(file_icon)
        post.icon = file_icon_url
        
        post.created = request.POST.get('created')
        post.updated = request.POST.get('updated')
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
        return HttpResponseRedirect('/home/categories-list')
    
    
    
def sub_test(request):
    if request.method == 'POST':
        post = SubCategories()
        post.category_id = request.POST.get('category')
        post.name_bangla= request.POST.get('name_bangla')
        post.name_english = request.POST.get('name_english')
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        post.image = file_url
        icon = request.FILES['icon']
        fss = FileSystemStorage()
        file_icon = fss.save(icon.name, icon)
        file_icon_url = fss.url(file_icon)
        post.icon = file_icon_url
        post.created = request.POST.get('created')
        post.updated = request.POST.get('updated')
        post.save()
    

    lists = Categories.objects.all().order_by('-id')
    args = {'lists': lists}
    return render(request, 'sub_categories/index.html', args)
        


def sub_list(request):
    lists = SubCategories.objects.all()
    args = {'lists': lists}
    return render(request, 'sub_categories/list.html', args)


def sub_test_2(request):
    if request.method == 'POST':
        post = SubCategories_2()
        post.category_id = request.POST.get('category')
        post.name_bangla = request.POST.get('name_bangla')
        post.name_english = request.POST.get('name_english')
        
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        post.image = file_url
        
        icon = request.FILES['icon']
        fss = FileSystemStorage()
        file_icon = fss.save(icon.name, icon)
        file_icon_url = fss.url(file_icon)
        post.icon = file_icon_url
        
        post.created = request.POST.get('created')
        post.updated = request.POST.get('updated')
        post.save()

    lists = SubCategories_2.objects.all().order_by('-id')
    args = {'lists': lists}
    return render(request, 'sub_categories_2/index.html', args)


def sub_list_2(request):
    lists = SubCategories_2.objects.all()
    args = {'lists': lists}
    return render(request, 'sub_categories_2/list.html', args)

