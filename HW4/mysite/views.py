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
    # tags = "<tr><td>Item Number</td><td>Brand Name</td><td>Price</td></tr>";
    # for product in products: 
    #     tags += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(product.sku, product.name, product.price);
    # return HttpResponse(html.format(tags));


def display_detail (request, sku): 
    try: 
        p = Product.objects.get(sku = sku);
        # tags = "<tr><td>Item Number</td><td>Brand Name</td><td>Price</td></tr>";
        # tags += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(product.sku, product.name, product.price);
        # return HttpResponse(html.format(product.name, tags));
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

def homepage (request): 
    return render(request, 'index.html', locals());

def show (request, id, name, age): 
    res = f"<h2>Hi, I'm {name}</h2>";
    res += "<ul>";
    res += f"   <li>age: {age}</li>";
    res += f"   <li>ID: {id}</li>";
    res += "</ul>";
    return HttpResponse(res);