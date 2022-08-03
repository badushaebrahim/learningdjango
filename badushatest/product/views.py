from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args,**kwargs):
    print(request)
    context ={
        'name':"badusha",
        'age':21,
        'values_list': [25,88,66]
    }
    
    return render(request,"homepage/home.html",context)

def contact_view(request,*args,**kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"homepage/contact.html",{})
