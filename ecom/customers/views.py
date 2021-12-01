from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import *
from .serializers import *
from django.shortcuts import render



def test(request):
    if request.method == 'POST':

        post = Customers()
        post.first_name = request.POST.get('first_name')
        post.last_name = request.POST.get('last_name')
        post.gender = request.POST.get('gender')
        
        picture = request.FILES['picture']
        fss = FileSystemStorage()
        file_picture = fss.save(picture.name, picture)
        file_picture_url = fss.url(file_picture)
        post.picture = file_picture_url
        
        post.dob= request.POST.get('dob')
        post.telephone = request.POST.get('telephone')
        post.fax = request.POST.get('fax')
        post.email_address = request.POST.get('email_address')
        post.password = request.POST.get('password')
        post.status = request.POST.get('status')
        
        post.save()

        return render(request, 'customers/index.html')

    else:

        return render(request, 'customers/index.html')


def list(request):
    lists = Customers.objects.all()
    args = {'lists': lists}
    return render(request, 'customers/list.html', args)
