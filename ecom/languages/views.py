from django.shortcuts import render
from .serializers import *
from .models import *

def test(request):
    if request.method=='POST':
       
        post = Languages()
        post.name = request.POST.get('name')
        post.code = request.POST.get('code')
        post.icon = request.POST.get('icon')
        post.directory = request.POST.get('directory ')
        post.save()
        
        return render(request, 'languages/index.html')
    
    else:
        
        return render(request, 'languages/index.html')

def list(request):
    lists =  Languages.objects.all()
    args = {'lists': lists}
    return render(request, 'languages/list.html', args)


def edit(request,pk):
    list = Languages.objects.filter(id=pk)
    args = {'lists': list}
    print(list)
    return render(request, 'languages/edit.html', args)
