from django.shortcuts import render
from .models import product

def index(request):
    products = product.objects.all()
    return render(request,'frontend/index.html', {'products':products})

def about(request):
    return render(request,'frontend/about.html')

def contact(request):
    return render(request,'frontend/contact.html')