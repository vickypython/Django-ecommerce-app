from django.shortcuts import render,get_list_or_404,redirect
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
def post_list(request):
    posts=Products.objects.all()
    return render(request,'customers/index.html',{"posts":posts})
def One_Post(request,post_id):
    post=get_list_or_404(Products,id=post_id)
    return render(request,'customers/index.html',{"posts":post})
def Create_post(request):
    if request.method == 'POST':
        name=request.POST['name']
        description=request.POST['description']
        Products.objects.create(name=name,description=description)
        return redirect('post_list')
    return render(request,'customers/index.html')


