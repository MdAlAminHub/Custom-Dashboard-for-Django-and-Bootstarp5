import json
from django.shortcuts import render
from django.http import JsonResponse
import datetime
from .models import *




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
    print('==========Filter Product=============', filter_product)
    
    context = {
        'filter_product': filter_product
    }
    return render(request, 'store/main.html', context)