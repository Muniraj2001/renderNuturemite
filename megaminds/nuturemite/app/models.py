from django.db import models
from django.contrib.auth.models import User

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
    ('WH','Women health')

}

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    images = models.ManyToManyField('ProductImage', blank=True, related_name='product_images')

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product/thumbnails')

    
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
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return self.name

class Product1(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
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
    def __str__(self):
        return self.name  

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
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
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
    image = models.ImageField(upload_to='product_images/')  # You need to create a 'product_images' directory in your media root
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)


class Specialoffer(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/')  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)    