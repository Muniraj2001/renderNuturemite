from calendar import c
from http.client import HTTPResponse
from pdb import post_mortem
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View

from .admin import CustomerModelAdmin

from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from .models import Coupon, Customer, DeliveryPartner, Orderplaced, Payment, Post, Product, Cart, ProductPricedrop, ShippingCharge, ShippingLabel, Wishlist, Popular, Shop, Post, BlogPost, Specialoffer,Post1,Review,Shopnow, RewardsPoints, StoreWallet, GiftVoucher  
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
from .forms import ContactForm
from .models import Post, Comment
from .models import Client
from .forms import ReviewForm
from .forms import PriceFilterForm



from random import sample

from django.db.models import F, FloatField, ExpressionWrapper

# @login_required
def home(request):
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))

    posts = Post1.objects.all()
    clients = Client.objects.all()
    product1 = ProductPricedrop.objects.get(pk=1)

    # Get all products ordered by discount_percentage in descending order
    products = Product.objects.annotate(
        discount_percentage_float=ExpressionWrapper(
            (F('selling_price') - F('discounted_price')) / F('selling_price') * 100,
            output_field=FloatField()
        )
    ).order_by('-discount_percentage_float')[:10]

    special_offers = Product.objects.all()

    # Get all Shopnow objects
    all_shopnows = Product.objects.all()

    # Randomly select 5 Shopnow objects
    special_offers = sample(list(special_offers), min(10, len(special_offers)))




  # Get all Shopnow objects
    all_shopnows = Product.objects.all()

    # Randomly select 5 Shopnow objects
    random_shopnows = sample(list(all_shopnows), min(5, len(all_shopnows)))






    return render(request, "app/home.html", {
        'products': products,
        'special_offers': special_offers,
        'posts': posts,
        'totalitem': totalitem,
        'wishitem': wishitem,
        'clients': clients,
        'shopnows': random_shopnows,
        'product1' : product1,
    })



@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post1, pk=post_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(post=post, author=request.user, content=content)

    return redirect('/')

# def view_comments(request, post_id):
#     post = get_object_or_404(Post1, pk=post_id)
#     comments = post.comments.all()  # Assuming the related_name in your Comment model is 'comments'
    
#     return render(request, 'app/view_comments.html', {'post': post, 'comments': comments})

def view_comments(request, post_id):
    post = get_object_or_404(Post1, pk=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        # Handle comment submission
        content = request.POST.get('content', '')
        Comment.objects.create(post=post, author=request.user, content=content)
        return JsonResponse({'status': 'success'})

    return render(request, 'app/view_comments.html', {'post': post, 'comments': comments})

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


# #     return render(request, 'app/contact.html')

# def contact(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         first_name = request.POST.get('fname', '')
#         last_name = request.POST.get('lname', '')
#         email = request.POST.get('email', '')
#         message = request.POST.get('message', '')

#         # Construct email message
#         email_subject = 'New Contact Form Submission'
#         email_message = f'Name: {first_name} {last_name}\nEmail: {email}\nMessage: {message}'

#         # Send email
#         send_mail(email_subject, email_message, 'munirajmechanical15@gmail.com', ['munirajmechanical15@gmail.com'])

#         # Redirect after successful submission
#         return HttpResponseRedirect(reverse('contact'))

#     # Render the form template for GET requests
#     return render(request, 'app/contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the email message
            email_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"

            # Send email
            send_mail(
                'Contact Form Submission',
                email_message,
                'munirajmechanical15@gmail.com',  # Replace with your email address
                ['munirajmechanical15@gmail.com'],  # Replace with the recipient's email address
                fail_silently=False,
            )

            return render(request, "app/home.html",locals())
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()

    return render(request, 'app/contact.html', {'form': form})
 

# @method_decorator(login_required, name='dispatch')
# class CategoryView(View):
#     def get(self, request, val):
#         totalitem = 0
#         wishitem = 0

#         if request.user.is_authenticated:
#             totalitem = len(Cart.objects.filter(user=request.user))
#             wishitem = len(Wishlist.objects.filter(user=request.user))

#         products = Product.objects.filter(category=val)
#         title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))

#         # Handle price filtering
        

#         return render(request, "app/category.html", locals())

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        products = Product.objects.filter(category=val)
        product1 = ProductPricedrop.objects.get(pk=1)

        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))

        # Handle price filtering
        # ...

        # Price filter
        price_filter = request.GET.get('price_filter', '_text_match:desc,weight:desc')
        if 'selling_price' in price_filter:
            # If the price filter is applied, update the queryset accordingly
            if price_filter == 'selling_price:asc':
                products = products.order_by('selling_price')
            elif price_filter == 'selling_price:desc':
                products = products.order_by('-selling_price')

        # Price range filter
        price_range = request.GET.get('price_range', '')
        if '-' in price_range:
            min_price, max_price = map(int, price_range.split('-'))
            products = products.filter(selling_price__gte=min_price, selling_price__lte=max_price)
        else:
            # Set default values if price_range is empty or doesn't contain a hyphen
            min_price, max_price = 0, 0

        # Dummy category counts (replace this with your actual logic to get category counts)
        category_counts = {'AN': 89}

        # Set the number of products to display per page
        products_per_page = 9
        paginator = Paginator(products, products_per_page)

        # Get the current page number
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If the page is not an integer, deliver the first page.
            products = paginator.page(1)
        except EmptyPage:
            # If the page is out of range, deliver the last page of results.
            products = paginator.page(paginator.num_pages)

        return render(request, 'app/category.html', {
            'products': products,
            'price_filter': price_filter,
            'min_price': min_price,
            'max_price': max_price,
            'category_counts': category_counts,
            'totalitem': totalitem,
            'wishitem': wishitem,
            'product1': product1,
        })
@method_decorator(login_required,name='dispatch')
class CategoryTitle(View):
    def get(self, request, val):
        products = Product.objects.filter(title=val)
        products = Product.objects.filter(title=val)

        title = Product.objects.filter(category=products[0].category).values('title')
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user)) 
        return render(request, "app/category.html", locals())

# @method_decorator(login_required, name='dispatch')
# class ProductDetail(View):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
#         totalitem = 0
#         wishitem = 0

#         if request.user.is_authenticated:
#             totalitem = len(Cart.objects.filter(user=request.user))
#             wishitem = len(Wishlist.objects.filter(user=request.user))
#         return render(request, "app/productdetail.html", locals())


from django.db.models import Count

@method_decorator(login_required, name='dispatch')
class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        products = ProductPricedrop.objects.get(pk=1)
        wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        # Get related products based on the current product's category
        related_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:15]

        # Get product reviews
        reviews = Review.objects.filter(product=product)

        # Calculate review counts for each rating
        rating_counts = reviews.values('rating').annotate(count=Count('rating'))

        # Review form for adding new reviews
        review_form = ReviewForm()
        reviews = reviews[::-1]

        return render(request, "app/productdetail.html", {
            'product': product,
            'wishlist': wishlist,
            'totalitem': totalitem,
            'wishitem': wishitem,
            'related_products': related_products,
            'reviews': reviews,
            'rating_counts': rating_counts,
            'review_form': review_form,
            'products' : products,
        })

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()

            messages.success(request, 'Review submitted successfully!')
        else:
            messages.error(request, 'Error submitting the review. Please check the form.')

        return redirect('product-detail', pk=pk)

class AddReview(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        review_form = ReviewForm()
        reviews = Review.objects.filter(product=product)

        return render(request, "app/add_review1.html", {
            'product': product,
            'review_form': review_form,
            'reviews': reviews,

        })

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()

            messages.success(request, 'Review submitted successfully!')
            return redirect('product-detail', pk=pk)
        else:
            messages.error(request, 'Error submitting the review. Please check the form.')

        return render(request, "app/add_review1.html", {
            'product': product,
            'review_form': form,
        })

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

class checkout(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40

        coupons = Coupon.objects.all()

        rewards_points = RewardsPoints.objects.get_or_create(user=user)[0].points
        store_wallet_balance = StoreWallet.objects.get_or_create(user=user)[0].balance
        gift_vouchers = GiftVoucher.objects.all()

        return render(request, 'app/checkout.html', locals())

    def post(self, request):
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40

        coupon_code = request.POST.get('coupon_code')
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code)
                if totalamount >= coupon.minimum_order_value:
                    discount_amount = (coupon.discount_percent / 100) * totalamount
                    totalamount -= discount_amount
                else:
                    messages.error(request, f"Minimum order value for coupon '{coupon_code}' not met.")
            except Coupon.DoesNotExist:
                messages.error(request, f"Invalid coupon code: {coupon_code}")

        rewards_points = RewardsPoints.objects.get_or_create(user=user)[0].points
        store_wallet_balance = StoreWallet.objects.get_or_create(user=user)[0].balance

        gift_voucher_code = request.POST.get('gift_voucher_code')
        if gift_voucher_code:
            try:
                gift_voucher = GiftVoucher.objects.get(code=gift_voucher_code)
                if totalamount >= gift_voucher.minimum_order_value:
                    totalamount -= min(totalamount, gift_voucher.value)
                else:
                    messages.error(request, f"Minimum order value for gift voucher '{gift_voucher_code}' not met.")
            except GiftVoucher.DoesNotExist:
                messages.error(request, f"Invalid gift voucher code: {gift_voucher_code}")

        razoramount = int(totalamount * 100)

        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = { "amount": razoramount, "currency": "INR","receipt": "order_rcptid_12"}
        payment_response = client.order.create(data=data)
        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
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

# ===============================================================================================================================================================
class checkout(View):
    @method_decorator(login_required)
    def get(self, request):
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0

        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value

        totalamount = famount + 40

        coupons = Coupon.objects.all()

        rewards_points = RewardsPoints.objects.get_or_create(user=user)[0].points
        store_wallet_balance = StoreWallet.objects.get_or_create(user=user)[0].balance
        gift_vouchers = GiftVoucher.objects.all()

        return render(request, 'app/checkout.html', locals())

    @method_decorator(login_required)
    def post(self, request):
        totalitem = 0
        wishitem = 0

        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))

        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0

        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value

        totalamount = famount + 40

        coupon_code = request.POST.get('coupon_code')
        if coupon_code:
            try:
                coupon = Coupon.objects.get(code=coupon_code)
                if totalamount >= coupon.minimum_order_value:
                    discount_amount = (coupon.discount_percent / 100) * totalamount
                    totalamount -= discount_amount
                else:
                    messages.error(request, f"Minimum order value for coupon '{coupon_code}' not met.")
            except Coupon.DoesNotExist:
                messages.error(request, f"Invalid coupon code: {coupon_code}")

        rewards_points = RewardsPoints.objects.get_or_create(user=user)[0].points
        store_wallet_balance = StoreWallet.objects.get_or_create(user=user)[0].balance

        gift_voucher_code = request.POST.get('gift_voucher_code')
        if gift_voucher_code:
            try:
                gift_voucher = GiftVoucher.objects.get(code=gift_voucher_code)
                if totalamount >= gift_voucher.minimum_order_value:
                    totalamount -= min(totalamount, gift_voucher.value)
                else:
                    messages.error(request, f"Minimum order value for gift voucher '{gift_voucher_code}' not met.")
            except GiftVoucher.DoesNotExist:
                messages.error(request, f"Invalid gift voucher code: {gift_voucher_code}")

        delivery_pincode = request.POST.get('delivery_pincode')
        if delivery_pincode:
            try:
                shipping_charge = ShippingCharge.objects.get(pincode=delivery_pincode).charge
                totalamount += float(shipping_charge)
            except ShippingCharge.DoesNotExist:
                messages.error(request, f"Shipping charge not available for pin code {delivery_pincode}")

        razoramount = int(totalamount * 100)

        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        data = {"amount": razoramount, "currency": "INR", "receipt": "order_rcptid_12"}
        payment_response = client.order.create(data=data)
        order_id = payment_response['id']
        order_status = payment_response['status']

        if order_status == 'created':
            payment = Payment(
                user=user,
                amount=totalamount,
                razorpay_order_id=order_id,
                razorpay_payment_status=order_status
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
        order_placed = Orderplaced.objects.create(
            user=user,
            customer=customer,
            product=c.product,
            quantity=c.quantity,
            payment=payment,
            status='Accepted'  # Set the initial status, you may update this based on your logic
        )
        
        # Assuming you have a way to determine the old status, replace 'OLD_STATUS' with the actual old status
        old_status = 'OLD_STATUS'  # Replace this with your logic to get the old status
        order_placed.send_status_notification(old_status)
        c.delete()

    # Send email notification for order placed
    subject = 'Order Placed Successfully'
    # message = 'Thank you for placing your order! Welcome to the Nuturemite website! 🌱 Thank you for choosing us and placing your order! 🛒 We re excited to have you as part of our community. At Nuturemite, we are dedicated to providing top-quality products that nurture and support your well-being. If you have any questions or need assistance, feel free to reach out to our friendly customer support team. 🌟 Happy shopping and thank you for trusting Nuturemite for your health and wellness needs! 🌿🌍'
    message = f'''
            Dear {user.username},

            🎉 Your order for {order_placed.product.title} has been placed successfully! 🎉
            Thank you for choosing Nuturemite! 🌱 Welcome to our community! 🛒

            At Nuturemite, we are dedicated to providing top-quality products that nurture and support your well-being. If you have any questions or need assistance, please don't hesitate to reach out to our friendly customer support team at:
            
            📞 Customer Care: 657878768
            📧 Customer Support Email: support@gmail.com

            Order Details:
            - Product: {order_placed.product.title}
            - Quantity: {order_placed.quantity}
            - Total Cost: ₹{order_placed.total_cost:.2f}

            🌿 Happy shopping and thank you for trusting Nuturemite for your health and wellness needs! 🌍

            Thank you for choosing Nuturemite!

            Sincerely,
            The Nuturemite Team
        '''

    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    try:
        print("Before send_mail")
        send_mail(subject, message, from_email, recipient_list)
        print("After send_mail")
    except Exception as e:
        print(f"Error sending email: {e}")

    # Send SMS notification for order placed
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body='Thank you for placing your order!',
            from_=settings.TWILIO_PHONE_NUMBER,
            to=user.profile.phone_number  # Assuming you have a phone_number field in your Customer model
        )
    except Exception as e:
        print(f"Error sending SMS: {e}")

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

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0

    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())

@method_decorator(login_required, name='dispatch')
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
def toggle_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        product = Product.objects.get(id=prod_id)
        user = request.user

        try:
            wishlist_item = Wishlist.objects.get(user=user, product=product)
            wishlist_item.delete()
            message = 'Item removed from wishlist.'
        except Wishlist.DoesNotExist:
            Wishlist(user=user, product=product).save()
            message = 'Item added to wishlist.'

        data = {
            'message': message,
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
    product1 = ProductPricedrop.objects.get(pk=1)

    price_filter = request.GET.get('price_filter', '_text_match:desc,weight:desc')
    if 'selling_price' in price_filter:
        # If the price filter is applied, update the queryset accordingly
        if price_filter == 'selling_price:asc':
            products = products.order_by('selling_price')
        elif price_filter == 'selling_price:desc':
            products = products.order_by('-selling_price')

    # Price range filter
    price_range = request.GET.get('price_range', '')
    if '-' in price_range:
        min_price, max_price = map(int, price_range.split('-'))
        products = products.filter(selling_price__gte=min_price, selling_price__lte=max_price)
    else:
        # Set default values if price_range is empty or doesn't contain a hyphen
        min_price, max_price = 0, 0

    # Dummy category counts (replace this with your actual logic to get category counts)
    category_counts = {'AN': 89}

    # Set the number of products to display per page
    products_per_page = 9
    paginator = Paginator(products, products_per_page)

    # Get the current page number
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        products = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, "app/search.html", {'query': query, 'totalitem': totalitem,'product1': product1, 'wishitem': wishitem, 'products': products,'price_filter': price_filter, 'min_price': min_price, 'max_price': max_price, 'category_counts': category_counts})    

# def latest_posts(request):
#     latest_posts = BlogPost.objects.all().order_by('-pub_date')[:5]  # Get the latest 5 posts
#     return render(request, 'latest_posts.html', {'latest_posts': latest_posts})



from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

from .models import Product

def shop(request):
    # Get all products
    products = Product.objects.all()
    product1 = ProductPricedrop.objects.get(pk=1)

    # Price filter
    price_filter = request.GET.get('price_filter', '_text_match:desc,weight:desc')
    if 'selling_price' in price_filter:
        # If the price filter is applied, update the queryset accordingly
        if price_filter == 'selling_price:asc':
            products = products.order_by('selling_price')
        elif price_filter == 'selling_price:desc':
            products = products.order_by('-selling_price')

    # Price range filter
    price_range = request.GET.get('price_range', '')
    if '-' in price_range:
        min_price, max_price = map(int, price_range.split('-'))
        products = products.filter(selling_price__gte=min_price, selling_price__lte=max_price)
    else:
        # Set default values if price_range is empty or doesn't contain a hyphen
        min_price, max_price = 0, 0

    # Dummy category counts (replace this with your actual logic to get category counts)
    category_counts = {'AN': 89}

    # Set the number of products to display per page
    products_per_page = 9
    paginator = Paginator(products, products_per_page)

    # Get the current page number
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        products = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'app/shop.html', {'products': products,'product1': product1, 'price_filter': price_filter, 'min_price': min_price, 'max_price': max_price, 'category_counts': category_counts})

def post_list(request):
    posts = Post1.objects.all()
    return render(request, 'app/blog.html', {'posts': posts})

def client_slider(request):
    clients = Client.objects.all()
    return render(request, 'your_app/client_slider.html', {'clients': clients})