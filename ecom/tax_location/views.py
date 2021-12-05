from django.shortcuts import render
from .models import *



def test(request):
    return render(request, 'countries/index.html')


def sub_test(request):
    if request.method == 'POST':

        post = TaxClasses()
        post.title = request.POST.get('title')
        post.description= request.POST.get('description')
        post.created = request.POST.get('created')
        post.updated = request.POST.get('updated')

        post.save()
        
    lists = TaxClasses.objects.all().order_by('-id')
    args = {'lists': lists}
    return render(request, 'tax_classes/index.html', args)

def sub_list(request):
    lists = TaxClasses.objects.all()
    args = {'lists': lists}
    return render(request,'tax_classes/list.html', args)


def tax_rates(request):
    return render(request, 'tax_rates/index.html')


def sub_list_2(request):
    # lists = TaxRates.objects.all()
    # # args = {'lists': lists}
    return render(request, 'tax_classes/list.html')


def zones(request):
    return render(request, 'zones/index.html')


