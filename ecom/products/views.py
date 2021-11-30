from django.shortcuts import render
from .models import *
from django.core.files.storage import FileSystemStorage
from manufacturer.models import Manufacturer
from tax_location.models import TaxClasses

def TEST(request):

    if request.method == 'POST':
        post = Product()
        # table coulumn name = form input name
        post.category_id = request.POST.get('category')  
        post.sub_category_id = request.POST.get('sub_category_id')
        post.manufacturars = request.POST.get('manufacturers_id')
        post.special = request.POST.get('special')
        post.product_name_english = request.POST.get('product_name_english')
        post.description_english = request.POST.get('description_english')
        post.product_name_bangla = request.POST.get('product_name_bangla')
        post.description_bangla = request.POST.get('description_bangla')
        post.tax_class = request.POST.get('tax_class')
        post.product_price = request.POST.get('product_price')
        post.product_weight = request.POST.get('product_weight')
        post.products_quantity = request.POST.get('products_quantity')
        post.offer_quantity_limit = request.POST.get('offer_quantity_limit')
        post.quantity_low_limit = request.POST.get('quantity_low_limit')

        image = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(image.name, image)
        file_url = fss.url(file)
        post.image = file_url
        post.status = request.POST.get('status')
        post.created = request.POST.get('created')
        post.updated = request.POST.get('updated')
        
        post.save()
        
        # return render(request, 'products/index.html')
    
    # else:
        
    lists = Categories.objects.all()
    subCategories = SubCategories.objects.all()
    manufactures = Manufacturer.objects.all()
    taxes = TaxClasses.objects.all()
    
    args = {
        'lists': lists,
        'subCategories': subCategories,
        'manufactures': manufactures,
        'taxes': taxes,
    
    }
    
    return render(request, 'products/index.html', args)


def list(request):
    lists = Product.objects.all()
    args = {'lists': lists}
    return render(request, 'products/list.html', args)

def sub_test(request):
    return render(request, 'product_attributes/index.html')

def sub_list(request):
    return render(request, 'product_attributes/list.html', )


