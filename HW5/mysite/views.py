from django.shortcuts import render
from django.http import HttpResponse, Http404
from mysite.models import Product
import random
from datetime import datetime
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

def index (request, tvno = 0): 
    tv_list = [{'name': 'Apple', 'tvcode': '0pg_Y41waaE'}, 
               {'name': 'Samsung', 'tvcode': 'RbQqok6_usY?si=bAlGyRnzFfwdO15U'}, 
               {'name': 'Sony', 'tvcode': '3gCKcq4THNQ?si=-mI8AAclgoa1hQ22'}, 
               {'name': 'Google', 'tvcode': 'otomCbnwsv0?si=3AeYa8Rs5ROP5hXa'}]
    now = datetime.now();
    tv = tv_list[tvno];
    quotes = ['Cat is cute', 
              'Dog is loyal', 
              'Fish is wet', 
              'Bird is free'];
    quote = random.choice(quotes);
    return render(request, 'index.html', locals());

def carlist (request, maker = 0): 
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ];
    car_list = [[], 
        ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
        ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
        ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
        ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
        ['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
            ];
    maker_name = car_maker[maker];
    cars = car_list[maker];
    return render(request, 'carlist.html', locals());

def carprice (request, maker = 0): 
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [[{'model':'Fiesta', 'price': 203500},
        {'model': 'Focus', 'price': 605000},
        {'model': 'Mustang', 'price': 900000}],
        [{'model': 'Fit', 'price': 450000},
        {'model': 'City', 'price': 150000},
        {'model': 'NSX', 'price': 1200000}],
        [{'model': 'Mazda3', 'price': 329999},
        {'model': 'Mazda5', 'price': 603000},
        {'model': 'Mazda6', 'price': 850000}],
            ];
    maker_name = car_maker[maker];
    cars = car_list[maker];
    return render(request, 'carprice.html', locals());






