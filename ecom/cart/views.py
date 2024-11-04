from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
# Create your views here.

def cart_summary(request):
    cart= Cart(request)
    cart_products=cart.get_prods
    return render(request,'cart_summary.html',{"cart_products": cart_products})


def cart_add(request):
    #get cart
    cart=Cart(request)
    #test for Post
    if request.POST.get('action')=='post':
        #get stuff
        product_id=int(request.POST.get('product_id'))
        #lookup product in DB
        product=get_object_or_404(Product,id=product_id)
        #Save to session
        cart.add(product=product)
        #Get Cart Quantity
        cart_quantity=cart.__len__()

        #Return response
        response=JsonResponse({'qty':cart_quantity})
        return response


def cart_delete():
    pass


def cart_update():
    pass