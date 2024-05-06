from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import Product
import random
# Create your views here.
def listing (request): 
    
    products = Product.objects.all();
    for p in products:
        if (p.size == 'S'): p.size = 'Small';
        elif (p.size == 'M'): p.size = 'Medium';
        elif (p.size == 'L'): p.size = 'Large';
    return render(request, 'list.html', locals());


def display_detail (request, sku): 
    try: 
        p = Product.objects.get(sku = sku);
        return render(request, 'display_detail.html', locals());
    except: 
        raise Http404("Cannot Find Specific Item Number.");

def about (request): 
    quotes = ['Cat is cute', 
              'Dog is loyal', 
              'Fish is wet', 
              'Bird is free'];
    quote = random.choice(quotes);
    return render(request, 'about.html', locals());