from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q
import json
import datetime



# Create your views here.
def home(request):
    return render(request, "landing.html")

@login_required(redirect_field_name="login_redirect", login_url="/login/")
def profile(request, slug):
    user = Customer.objects.filter(slug=slug)
    address = user[0].user_address
    gender = user[0].user_gender
    image = user[0].user_profile
    phone = user[0].user_phone
    username = User.objects.filter(username=slug)[0].username
    fullname = User.objects.filter(username=slug)[0].get_full_name()
    context = {"gender": gender, "address": address, "title": f"Profile | @ {username}", "fullname": fullname, "profile":image, "phone":phone}
    return render(request, "profile.html", context)


class Store(ListView):
    model = Product
    template_name = "store.html"
    extra_context={'banners': Banner.objects.all(), 'order':Order.objects.all()}

    # Search query for class based views
    def get_queryset(self):  # new
        query = self.request.GET.get("q", None)
        if query:
            object_list = Product.objects.filter(
                Q(product_name__icontains=query) | Q(product_description__icontains=query)
            )
            return object_list
        else:
            object_list = Product.objects.all()
            return object_list





@login_required(redirect_field_name="login_redirect", login_url="/login/")
def cart_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        messages.info(request,"Login to add items in cart")
        items=[]
        order={'get_sub_total': 0, 'get_total': 0, 'get_total_items': 0}
    context={'items': items, 'order': order}
    return render(request, "cart.html", context)


# Cart functionality views:
def update_item(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if(action=='add'):
        orderItem.quantity = (orderItem.quantity + 1)
        messages.success(request, "Item Added successfully")
    elif(action=='sub'):
        orderItem.quantity = (orderItem.quantity - 1)
        messages.success(request, "Item decremented successfully")


    orderItem.save()

    if(action == 'rm'):
        orderItem.delete()
        messages.success(request, "Item deleted successfully")


    if(orderItem.quantity <= 0):
        orderItem.delete()
        messages.success(request, "Item deleted successfully")

   

    

    return JsonResponse("Item added to cart", safe=False)



# Will require an id
class ProductDetailView(DetailView):
    model = Product
    template_name = "description.html"


# Will require an id
# @method_decorator(login_required(login_url='/login/'), name='dispatch')
@login_required(redirect_field_name="login_redirect", login_url="/login/")
def checkout_page(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items=[]
        order={'get_sub_total': 0, 'get_total': 0}
    context={'items': items, 'order': order}
    return render(request, "checkout.html", context)

# Order processing view
def process_order(request):
    orderid = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['total'])
        order.orderid = orderid

        if total == order.get_total():
            order.complete = True
        order.save()

        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address = data['address'],
            phone = data['phone'],
        )

    else:
        messages.error(request, "You are not logged in")
    return JsonResponse(f"Order Processed {data}", safe=False)

def login_view(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        # Check if email is valid or not
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request, "Invalid Username")
            return redirect("/login/")

        # Checck if password and email is valid or not
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        
        # If both checks are passed then login the user
        else:
            login(request, user)
            return redirect("/shop/")
    if request.user.is_authenticated :
        messages.info(request, "Already Logged In")
        return redirect("/")
    else:
        return render(request, "login.html", context={"title": "Login"})

def signup_view(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        profile = request.FILES.get("profile")
        email = data.get("email")
        password = data.get("password")
        gender = data.get("gender")
        address = data.get("address")
        phone = data.get("phone")


        

        # Email exist check
        user = User.objects.filter(email=email)
        if user.exists():
            messages.error(request, "User with this email already exists!")
            return redirect("/signup/")
        
        # Username exist check
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "User with this username already exists!")
            return redirect("/signup/")

        # After validations saving the new user in db:
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username)
        user.set_password(password)
        user.save()

        user_info = Customer.objects.create(user_gender=gender, user_profile=profile , user_address=address, user_phone=phone, slug=username)

        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/shop/")
        
    if request.user.is_authenticated :
        messages.info(request, "Already Logged In")
        return redirect("/")
    else:
        return render(request, "register.html", context={"title": "Register"})


def logout_view(request):
    logout(request)
    return redirect("/login")