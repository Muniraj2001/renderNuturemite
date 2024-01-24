from audioop import avg
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
from twilio.rest import Client
STATE_CHOICES = {
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'), ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'), 
    ('Chattisgarh', 'Chattisgarh'), 
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), 
    ('Daman and Diu', 'Daman and Diu'), 
    ('Delhi', 'Delhi'), ('Goa', 'Goa'), 
    ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'), 
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
}

CATEGORY_CHOICES={
    ('AN','Antioxidants'),
    ('AV','Ayurvedic'),
    ('DH','Digestive Health'),
    ('GH','General Health'),
    ('HS','Herbal, Specialty Supplements'),
    ('IH','Immune Health'),
    ('MH','Men Health'),
    ('OG','Organic'),
    ('PC','Personal Care'),
    ('SH','Sexual health'),
    ('VM', 'Vitamins&Minerals'),
    ('WH','Women health'),

    ('B12','Vitamin B12'),
    ('C','Vitamin C'),
    ('D3','Vitamin D3'),
    ('E','Vitamin E'),
    ('A','Vitamin A'),
    ('C','Vitamin C'),
    ('K','Vitamin K'),
    
    

    

}

from django.db import models

from django.db import models
from django.db.models import Avg

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to='product')
    images = models.ManyToManyField('ProductImage', blank=True, related_name='product_images')

    
    def discount_percentage(self):
        if self.is_sale and self.sale_price:
            discount = ((self.price - self.sale_price) / self.price) * 100
            return round(discount, 2)
        return None
    
    @property
    def discount_percentage(self):
        if self.selling_price and self.discounted_price:
            discount = ((self.selling_price - self.discounted_price) / self.selling_price) * 100
            return round(discount, 2)
        return 0
    def average_rating(self):
        if self.reviews.count() > 0:
            total_ratings = sum([review.rating for review in self.reviews.all()])
            return total_ratings / self.reviews.count()
        else:
            return 0
        
        

    def stars(self):
        average_rating = self.average_rating()
        full_stars = int(average_rating)
        has_half_star = round((average_rating % 1) * 2)  # round to 0 or 1
        empty_stars = 5 - full_stars - has_half_star

        return {
            'full_stars': range(full_stars),
            'has_half_star': has_half_star,
            'empty_stars': range(empty_stars),
        }

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product/thumbnails')

class ProductPricedrop(models.Model):
    category = models.CharField(max_length=255)
    price_drop_percentage = models.FloatField()
    sale_end_time = models.DateTimeField()

    def remaining_time(self):
        now = timezone.now()
        time_difference = self.sale_end_time - now

        days, seconds = divmod(time_difference.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        return f"{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s"

    def __str__(self):
        return self.category


class Shop(models.Model):
    CATEGORY_CHOICES = (
        ('AN','Antioxidants'),
        ('AV','Ayurvedic'),
        ('DH','Digestive Health'),
        ('GH','General Health'),
        ('HS','Herbal, Specialty Supplements'),
        ('IH','Immune Health'),
        ('MH','Men Health'),
        ('OG','Organic'),
        ('PC','Personal Care'),
        ('SH','Sexual health'),
        ('VM', 'Vitamins&Minerals'),
        ('WH','Women health')
    )

    name = models.CharField(max_length=255)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)


    def discount_percentage(self):
        if self.is_sale and self.sale_price:
            discount = ((self.price - self.sale_price) / self.price) * 100
            return round(discount, 2)
        return None
    
    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.title}'

class Product1(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    main_image = models.ImageField(upload_to='product_images/')
    thumb1 = models.ImageField(upload_to='product_images/')
    thumb2 = models.ImageField(upload_to='product_images/')
    thumb3 = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
        

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    pincode = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name  
class ShippingCharge(models.Model):
    pincode = models.CharField(max_length=10, unique=True)
    charge = models.DecimalField(max_digits=6, decimal_places=2)
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price      

STATUS_CHOICES={
    ('Accepted','Accepted'),
    ('Packed', 'packed'),
    ('On The Wey', 'On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
}    
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.PositiveIntegerField(default=0)
    minimum_order_value = models.FloatField(default=0)
    expiration_date = models.DateTimeField(default=timezone.now)  # Add this line for the expiration date

    def is_valid(self):
        return self.expiration_date >= timezone.now()

class RewardsPoints(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

class StoreWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

class GiftVoucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    value = models.FloatField(default=0)
    minimum_order_value = models.FloatField(default=0)

class Payment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class Orderplaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    rewards_points = models.PositiveIntegerField(default=0)
    store_wallet_balance = models.FloatField(default=0)
    gift_voucher = models.ForeignKey(GiftVoucher, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_pincode = models.CharField(max_length=10)

    def send_status_notification(self, old_status):
        user_email = self.user.email
        try:
            user_profile = self.user.profile
            user_phone_number = user_profile.phone_number
        except AttributeError:
            user_profile = None
            user_phone_number = None

        # Check if the status has changed
        if self.status != old_status:
            # Email notification
            subject = f'Order Status Update: {self.status}'
            # message = f'Your order for {self.product.title} is {self.status.lower()}. Thank you for shopping with us!'
            message = f'''
            Dear {self.user.username},

            Thank you for choosing Nuturemite! Your order for {self.product.title} has been {self.status.lower()}.

            ═══════════════════════════════════════════════════════
            Order Details:
            Product: {self.product.title}
            Quantity: {self.quantity}
            Total Cost: ₹{self.total_cost:,.2f}
            ═══════════════════════════════════════════════════════

            Your order is being processed and will be shipped to you soon. We appreciate your business!

            If you have any questions or concerns, our customer support team is here to help.

            📞 Customer Support: 1-800-123-4567
            📧 Email: support@nuturemite.com

            Thank you again for choosing Nuturemite. We look forward to serving you again!

            Best regards,
            The Nuturemite Team
            '''
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email])

            # WhatsApp/SMS notification
            if user_phone_number:
                account_sid = settings.TWILIO_ACCOUNT_SID
                auth_token = settings.TWILIO_AUTH_TOKEN
                client = Client(account_sid, auth_token)

                try:
                    message = client.messages.create(
                        body=f'Your order for {self.product.title} is {self.status.lower()}. Thank you for shopping with us!',
                        from_=settings.TWILIO_PHONE_NUMBER,
                        to=user_phone_number
                    )
                except Exception as e:
                    print(f"Error sending SMS: {e}")

    def save(self, *args, **kwargs):
        # Get the old status before saving
        old_status = Orderplaced.objects.get(pk=self.pk).status if self.pk else None

        super().save(*args, **kwargs)

        # Check if the status has changed after saving
        if old_status is not None:
            self.send_status_notification(old_status)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price 
     
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)    


# class BlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     category = models.CharField(max_length=100)
#     content = models.TextField()
#     pub_date = models.DateField()
#     author = models.CharField(max_length=100)
#     comment_count = models.IntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return self.title
    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateField()
    author = models.CharField(max_length=100)
    comments = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

class Popular(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)

    def discount_percentage(self):
        if self.is_sale and self.sale_price:
            discount = ((self.price - self.sale_price) / self.price) * 100
            return round(discount, 2)
        return None

class Specialoffer(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)    

    def discount_percentage(self):
        if self.is_sale and self.sale_price:
            discount = ((self.price - self.sale_price) / self.price) * 100
            return round(discount, 2)
        return None
    
class Shopnow(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)    

    def discount_percentage(self):
        if self.is_sale and self.sale_price:
            discount = ((self.price - self.sale_price) / self.price) * 100
            return round(discount, 2)
        return None
    
    

class Post1(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post1, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}' 


class Client(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name       
    
class ShippingLabel(models.Model):
    order = models.ForeignKey(Orderplaced, on_delete=models.CASCADE)
    label_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class DeliveryPartner(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

class OrderNotification(models.Model):
    order = models.ForeignKey(Orderplaced, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

class WhatsAppChat(models.Model):
    order = models.ForeignKey(Orderplaced, on_delete=models.CASCADE)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    