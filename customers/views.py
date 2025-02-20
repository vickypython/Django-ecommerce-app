from django.shortcuts import render
from django.http import HttpResponse
from .models import Categorie,Products
# Create your views here.
def say_hello(request):
    categories=Categorie.objects.all()
    products=Products.objects.all()
    context={
        'categories':categories,
        'products':products
    }
    return render(request,'customers/index.html',context)