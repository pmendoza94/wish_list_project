from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..user_app.models import User
from .models import Product

# Create your views here.
def sessionChecker(request):
    try:
        return request.session['user_id']
    except:
        return False

def index(request):
    if sessionChecker(request) == False:
        return redirect('/')
    # Product.objects.all().delete()

    created_product = []
    user = User.objects.get(id = request.session['user_id'])
    # for product in Product.objects.all():
    #     print product.added_by.first(), product.product_name
        # if user in product.added_by.all()[:0]:
        #     created_product.append(product)

    print created_product
    context = {
        'user': User.objects.get(id = request.session['user_id']),
        # 'users': User.objects.all(),
        'products': Product.objects.all(),
        # 'products': Product.objects.exclude(id = request.session['user_id']),
    }

    return render(request, 'product_app/index.html', context)

def create(request):
    if sessionChecker(request) == False:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    return render(request, 'product_app/add.html')

def create_process(request):
    results = Product.objects.createVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/wishlist/create')

    else:
        user = User.objects.get(id = request.session['user_id'])
        item = Product.objects.create(product_name = request.POST['product_name'])
        item.added_by.add(user)
        return redirect('/wishlist')

def wish_item(request, product_id):
    if sessionChecker(request) == False:
        return redirect('/')

    context = {
        'product': Product.objects.get(id = product_id),
    }

    return render(request, 'product_app/product.html', context)

def add(request, product_id, user_id):
    User.objects.get(id = user_id).users.add(Product.objects.get(id = product_id))
    print Product.objects.get(id = product_id).added_by, '~~~~~~~~~~~'
    return redirect('/wishlist')

def remove(request, product_id, user_id):
    Product.objects.get(id = product_id).added_by.remove(User.objects.get(id = user_id))
    return redirect('/wishlist')

def delete(request, product_id, user_id):
    Product.objects.get(id = product_id).delete()
    # User.objects.get(id = user_id).users.delete(Product.objects.get(id = product_id))
    return redirect('/wishlist')
