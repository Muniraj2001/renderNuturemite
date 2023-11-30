from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from . models import Product, Customer, Cart, Payment, Orderplaced, ProductImage, Wishlist, Product1, Shop, Post, BlogPost, Popular, Specialoffer
from django.contrib.auth.models import Group

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 4  # Adjust as needed

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ['id', 'title', 'discounted_price', 'category', 'display_product_image']

    def display_product_image(self, obj):
        if obj.product_image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.product_image.url)
        return 'No Image'

    display_product_image.short_description = 'Product Image'

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'display_image']

    def display_image(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)

    display_image.short_description = 'Image'

@admin.register(Product1)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price']



@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_sale', 'sale_price')
    list_filter = ('is_sale',)
    search_fields = ('name',)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','city','state','zipcode']    

@admin.register(Cart)
class CartModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product','quantity']
    # def products(self,obj):
    #     link = reverse("admin:app_product_change",args=[obj.product.pk])
    #     return format_html('<a href="{}>"{}</a>',link, obj.product.title)

@admin.register(Payment)
class paymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']    



# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'pub_date', 'author', 'comment_count')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'author')
    search_fields = ('title', 'author')
    list_filter = ('date_posted',)


@admin.register(Orderplaced)
class Orderplaced(admin.ModelAdmin):
    list_display = ['id','user','customers','products','quantity','ordered_date','status','payments']
    def customers(self,obj):
        link = reverse("admin:app_product_change",args=[obj.customer.pk])
        return format_html('<a href="{}>"{}</a>',link, obj.customer.name)
    
    def products(self,obj):
        link = reverse("admin:app_product_change",args=[obj.product.pk])
        return format_html('<a href="{}>"{}</a>',link, obj.payment.razorpay_payment_id)
    
    def payments(self,obj):
        link = reverse("admin:app_payment_change",args=[obj.product.pk])
        return format_html('<a href="{}>"{}</a>',link, obj.product.title)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    search_fields = ('title', 'content')

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','products']  
    def products(self,obj):
        link = reverse("admin:app_products_change",args=[obj.product.pk])
        return format_html('<a href="{}>"{}</a>',link, obj.product.title) 
    
admin.site.unregister(Group )

@admin.register(Popular)
class PopularAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sale_price', 'is_sale', 'category')
    search_fields = ['name', 'category']
    list_filter = ['is_sale', 'category']

@admin.register(Specialoffer)
class SpecialofferAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sale_price', 'is_sale', 'category')
    search_fields = ['name', 'category']
    list_filter = ['is_sale', 'category']    