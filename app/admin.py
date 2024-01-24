from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from . models import Product, Customer, Cart, Payment, Orderplaced, ProductImage, ProductPricedrop, ShippingCharge, Wishlist, Product1, Shop, Post, BlogPost, Popular, Specialoffer,Comment, Post1,Shopnow, RewardsPoints, StoreWallet, GiftVoucher
from django.contrib.auth.models import Group
from .models import Client

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

class ProductPricedropAdmin(admin.ModelAdmin):
    list_display = ('category', 'price_drop_percentage', 'remaining_time')
    search_fields = ('category',)

admin.site.register(ProductPricedrop, ProductPricedropAdmin)

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


# @admin.register(Orderplaced)
# class Orderplaced(admin.ModelAdmin):
#     list_display = ['id','user','customers','products','quantity','ordered_date','status','payments']
#     def customers(self,obj):
#         link = reverse("admin:app_product_change",args=[obj.customer.pk])
#         return format_html('<a href="{}>"{}</a>',link, obj.customer.name)
    
#     def products(self,obj):
#         link = reverse("admin:app_product_change",args=[obj.product.pk])
#         return format_html('<a href="{}>"{}</a>',link, obj.payment.razorpay_payment_id)
    
#     def payments(self,obj):
#         link = reverse("admin:app_payment_change",args=[obj.product.pk])
#         return format_html('<a href="{}>"{}</a>',link, obj.product.title)

@admin.register(Orderplaced)
class Orderplaced(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_customer_address', 'get_product', 'quantity', 'ordered_date', 'status', 'get_payment']

    def get_customer_address(self, obj):
        return f"{obj.customer.name}, {obj.customer.locality}, {obj.customer.city}, {obj.customer.state} - {obj.customer.zipcode}"

    def get_customer(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def get_product(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def get_payment(self, obj):
        link = reverse("admin:app_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)

    get_customer_address.short_description = 'Customer Address'

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
@admin.register(Shopnow)
class ShopnowAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sale_price', 'is_sale', 'category')
    search_fields = ['name', 'category']
    list_filter = ['is_sale', 'category'] 

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


class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Post1)
class Post1Admin(admin.ModelAdmin):
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'content', 'posted_date']    


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',) 

from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'minimum_order_value')
    search_fields = ('code',)     

@admin.register(RewardsPoints)
class RewardsPointsAdmin(admin.ModelAdmin):
    list_display = ['user', 'points']

@admin.register(StoreWallet)
class StoreWalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']

@admin.register(GiftVoucher)
class GiftVoucherAdmin(admin.ModelAdmin):
    list_display = ['code', 'value', 'minimum_order_value']    


class ShippingChargeAdmin(admin.ModelAdmin):
    list_display = ('pincode', 'charge')

admin.site.register(ShippingCharge, ShippingChargeAdmin)    