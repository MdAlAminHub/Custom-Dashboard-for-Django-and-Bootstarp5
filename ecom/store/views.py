import json
from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import JsonResponse
import datetime
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm

from django.shortcuts import render
# from django.core.files.storage import FileSystemStorage
from .models import *
# from .serializers import *


def customer_detail(request):
    if request.method == 'POST':

        post = Customer()
        
        post.username = request.POST.get('username')
        post.first_name = request.POST.get('first_name')
        post.last_name = request.POST.get('last_name')
        post.telephone = request.POST.get('telephone')
        post.email_address = request.POST.get('email_address')
        post.password = request.POST.get('password')
        post.conf_password = request.POST.get('conf_password')

        post.save()

        # return render(request, 'customers/index.html')

    else:
        return render(request, 'store/main.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST["username"],
        first_name = request.POST["first_name"],
        
        last_name = request.POST["last_name"],
        
        telephone = request.POST["telephone"],
        email_address = request.POST["email_address"], 
        # password = request.POST["password"],
        conf_password = request.POST["conf_password"]
        password = make_password(request.POST["password"])
        
        # user = User.objects.create(username=username, first_name=first_name, last_name=last_name, password=password1)
        # # , password=password1
        # # user.set_password(password1)
        # user.save()
    
        # print("===========user==========")
        # print(user)
        # print('User Created')
        customer = Customer.objects.create(
            username=username, first_name=first_name, last_name=last_name, telephone=telephone, email_address=email_address,password=password, conf_password=conf_password)
        customer.save()
        
        return redirect('/')
    return render(request, 'store/main.html')

    print('Password not matching!')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        

        customer = Customer.objects.get(username=username)
        # print("username", customer)

        # user = auth.authenticate(username=username, password=password)
        if customer is not None:
            # auth.login(request, customer)
            return redirect('/')
        messages.Info('Invalid credentials')
        return redirect('/')
    return render(request, 'store/main.html')
            

def logout_view(request):
    logout(request)
    return redirect('/')
    

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
        
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        print('==============Customer============', customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order.get_cart_items
        
    context = {'items': items, 'order':order, 'cartItems':cartItems}
    
    return render(request, 'store/cart.html', context)


def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order.get_cart_items

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        
           
    
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    else:
        print('User is not logged in ..')      
            
    return JsonResponse('Payment complete!', safe=False)
    
 
 
def get_general_product(request):
    category_obj = Categories.objects.get(name_english='General Grocery')
    sub_category_obj = SubCategories.objects.filter(category=category_obj)
    context = {
        'sub_category_obj': sub_category_obj
    }
    return render(request, 'store/main.html', context)


def get_cooking_essentials(request):
    cooking_obj = Categories.objects.get(name_english='Cooking Essential')
    cooking_obj_list = SubCategories.objects.filter(category=cooking_obj)
    context = {
        'cooking_obj_list': cooking_obj_list
    }
    return render(request, 'store/main.html', context)


def get_home_care(request):
    home_care_obj = Categories.objects.get(
        name_english='Home Care and Cleaning Utilities')
    home_care_obj_list = SubCategories.objects.filter(category=home_care_obj)
    context = {
        'home_care_obj_list': home_care_obj_list
    }
    return render(request, 'store/main.html', context)



    
     
     
def get_filterd_product(request, id):
    sub_obj = SubCategories.objects.get(id=id)
    filter_product = Product.objects.filter(subcategory=sub_obj)
    context = {
        'filter_product': filter_product
    }
    return render(request, 'store/main.html', context)
