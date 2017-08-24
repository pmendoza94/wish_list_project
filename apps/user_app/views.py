from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    #This is to clear the db if needed!
    # User.objects.all().delete()
    return render(request, 'user_app/index.html')

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
    else:
        messages.success(request, 'User has been created! Please login to continue')
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['user_id'] = results['user'].id
        request.session['user_name'] = results['user'].name
        return redirect('/wishlist')


def logout(request):
    request.session.flush()
    return redirect('/')
