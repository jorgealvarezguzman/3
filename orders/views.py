from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from orders.forms import RegisterForm

from .models import *

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html")
    context = {
        "products": Product.objects.all()
    }
    return render(request, "user.html", context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
        return redirect('index')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form': form})


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})


def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart_detail.html')


@login_required(login_url="/users/login")
def create_order(request):
    cart = Cart(request)
    total_price = 0

    order = Order.objects.create(total_price=total_price)

    for key, value in cart.cart.items():
        total_price += float(value['price']) * value['quantity']
        product = Product.objects.get(id=key)
        order.cart.add(product)

    order.total_price = total_price
    order.save()

    cart.clear()

    return redirect("index")
