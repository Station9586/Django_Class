from django.shortcuts import render
from DB.models import *
# Create your views here.

def index (request): 
    products = Product.objects.all()
    return render(request, 'index.html', locals())


def detail (request, id): 
    try: 
        product = Product.objects.get(id = id)
        images = PPhoto.objects.filter(product = product)
    except: 
        pass
    return render(request, 'detail.html', locals())
