from http.client import HTTPResponse
from pdb import post_mortem
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from .models import Customer, Orderplaced, Payment, Post, Product, Cart, Wishlist, Popular, Shop, Post, BlogPost, Specialoffer  
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.conf import settings
import razorpay
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseBadRequest
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail



@login_required
def home(request):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    posts = BlogPost.objects.all()
    products = Popular.objects.all()
    special_offers = Specialoffer.objects.all()

    return render(request, "app/home.html", {'products': products, 'special_offers': special_offers,'posts':posts, 'totalitem': totalitem, 'wishitem': wishitem})    # return render(request, "app/home.html",locals())

@login_required
def about(request):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, "app/about.html",locals())

@login_required

# def contact(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         user_email = request.POST.get('user_email')
#         user_message = request.POST.get('user_message')

#         print(f"Name: {user_name}, Email: {user_email}, Message: {user_message}")


#     return render(request, 'app/contact.html')

def contact(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('fname', '')
        last_name = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Construct email message
        email_subject = 'New Contact Form Submission'
        email_message = f'Name: {first_name} {last_name}\nEmail: {email}\nMessage: {message}'

        # Send email
        send_mail(email_subject, email_message, 'munirajmechanical15@gmail.com', ['munirajmechanical15@gmail.com'])

        # Redirect after successful submission
        return HttpResponseRedirect(reverse('contact'))

    # Render the form template for GET requests
    return render(request, 'app/contact.html')

@method_decorator(login_required,name='dispatch')
class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        products = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())

@method_decorator(login_required,name='dispatch')
class CategoryTitle(View):
    def get(self, request, val):
        products = Product.objects.filter(title=val)
        title = Product.objects.filter(category=products[0].category).values('title')
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user)) 
        return render(request, "app/category.html", locals())

@method_decorator(login_required, name='dispatch')
class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, "app/productdetail.html", locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/customerregistration.html', locals())

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User registered successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/customerregistration.html', locals())

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile saved successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/profile.html', locals())

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())

@method_decorator(login_required,name='dispatch')
class UpdateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
           totalitem = len(Cart.objects.filter(user=request.user))
           wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/updateAddress.html', locals())

    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Congratulations! Profile updated successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('prod_id')

        try:
            product = Product.objects.get(id=product_id)

            Cart(user=user, product=product).save()

            return redirect(reverse('cart'))
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Invalid product ID")
    else:
        return HttpResponseBadRequest("Invalid request method")


@login_required
def cart_view(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40   
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user)) 
    return render(request, 'app/addtocart.html', locals())

@login_required
def show_wishlist(request):
    user = request.user
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    product = Wishlist.objects.filter(user=user)
    return render(request,"app/Wishlist.html",locals())    

@method_decorator(login_required,name='dispatch')
class checkout(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        user=request.user
        add=Customer.objects.filter(user=user)
        cart_items=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40   
        razoramount = int(totalamount * 100) 
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = { "amount": razoramount, "currency": "INR","receipt": "order_rcptid_12"}
        payment_response = client.order.create(data=data)
        print(payment_response)
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user = user,
                amount = totalamount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status
            )
            payment.save()
        return render(request, 'app/checkout.html', locals())

@login_required    
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id').strip('${}')  
    user = request.user

    if not user.is_authenticated:
        return redirect("login")  

    try:
        customer = Customer.objects.get(id=cust_id)
    except Customer.DoesNotExist:
        return redirect("error_page")  

    try:
        payment = Payment.objects.get(razorpay_order_id=order_id)
    except Payment.DoesNotExist:
        return redirect("error_page")  
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()

    cart = Cart.objects.filter(user=user)

    for c in cart:
        Orderplaced.objects.create(
            user=user,
            customer=customer,
            product=c.product,
            quantity=c.quantity,
            payment=payment
        )
        c.delete()

    return redirect("orders")

@login_required
def orders(request):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    order_placed=Orderplaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        user = request.user
        carts = Cart.objects.filter(Q(product=prod_id) & Q(user=user))

        if carts.exists():
            c = carts.first()
        else:
            c = Cart.objects.create(product=prod_id, user=user, quantity=1)

        c.quantity += 1
        c.save()

        cart = Cart.objects.filter(user=user)
        amount = sum(p.quantity * p.product.discounted_price for p in cart)
        totalamount = amount + 40 * len(cart)

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }

        return JsonResponse(data)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        carts = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))

        if carts.exists():
            carts.delete()
            success_message = "Cart item(s) removed successfully"
        else:
            success_message = "No matching cart items found"

        cart = Cart.objects.filter(user=request.user)
        amount = sum(p.quantity * p.product.discounted_price for p in cart)
        totalamount = amount + 40

        data = {
            'success_message': success_message,
            'amount': amount,
            'totalamount': totalamount
        }

        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        carts = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))

        if carts.exists():
            c = carts.first()
            if c.quantity > 1:
                c.quantity -= 1
                c.save()
                success_message = "Quantity decreased successfully"
            else:
                c.delete()
                success_message = "Cart item removed successfully"
        else:
            success_message = "No matching cart items found"
            c = Cart()

        cart = Cart.objects.filter(user=request.user)
        amount = sum(p.quantity * p.product.discounted_price for p in cart)
        totalamount = amount + 40

        data = {
            'success_message': success_message,
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }

        return JsonResponse(data)

def plus_wishlist(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user,product=product).save()
        data={
            'message':'Wishlist Added Successfully',
        }
        return JsonResponse(data)
    
def minus_wishlist(request):
    if request.method == 'GET':
        prod_id=request.GET['prod_id']
        product=Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user,product=product).delete()
        data={
            'message':'Wishlist Remove Successfully',
        }    
        return JsonResponse(data)

@login_required    
def search(request):
    query = request.GET.get('search', '')  
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = Cart.objects.filter(user=request.user).count()
        wishitem = Wishlist.objects.filter(user=request.user).count()

    products = Product.objects.filter(Q(title__icontains=query))

    return render(request, "app/search.html", {'query': query, 'totalitem': totalitem, 'wishitem': wishitem, 'products': products})    

# def latest_posts(request):
#     latest_posts = BlogPost.objects.all().order_by('-pub_date')[:5]  # Get the latest 5 posts
#     return render(request, 'latest_posts.html', {'latest_posts': latest_posts})



def shop(request):
    products = Shop.objects.all()
    return render(request, 'app/shop.html', {'products': products})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'app/blog.html', {'posts': posts})