from django.shortcuts import render
#from django.http import HttpResponse
from .models import Product
# Create your views here.


def home_view(request):
    print(request)
    context ={
        'name':"badusha",
        'age':21,
        'values_list': [25,88,66]
    }
    
    return render(request, "homepage/home.html", context)


def contact_view(request):
    print(request.user)
    return render(request, "homepage/contact.html", {})

#product view thats shows one product details

def product_view(request):
    obj = Product.objects.get(id =1)
    context = {
        'object':obj
        }
    return render(request, "homepage/product.html", context)