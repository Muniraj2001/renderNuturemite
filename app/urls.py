from django.urls import path

from django.contrib import admin
from .forms import LoginForm, MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm

from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_view
from .views import add_comment
from .views import view_comments
from .views import client_slider
from .views import toggle_wishlist
from .views import AddReview

# from .views import contact, chatbot


urlpatterns = [
    path("",views.home),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    # path('contact_success/', views=contact_success, name='contact_success'),
    path("category/<slug:val>",views.CategoryView.as_view(),name='category'),
    path("category/-title/<val>",views.CategoryTitle.as_view(),name='category-title'),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    # path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('address', views.address, name='address'),
    path('updateAddress/<int:pk>', views.UpdateAddress.as_view(), name='updateAddress'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('view_comments/<int:post_id>/', view_comments, name='view_comments'),
    path('client-slider/', client_slider, name='client_slider'),
    path('togglewishlist/', toggle_wishlist, name='toggle-wishlist'),
    path('add-review/<int:pk>/', AddReview.as_view(), name='add-review'),

    #cart
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/',views.orders, name='orders'),

    path('search/',views.search,name='search'),
    path('wishlist/', views.show_wishlist, name='showwishlist'),
    
    # path('chatbot/', chatbot, name='chatbot'),

    path('pluscart/', views.plus_cart, name='plus_cart'),
    path('minuscart/', views.minus_cart, name='minus_cart'),
    path('removecart/', views.remove_cart, name='remove_cart'),
    path('pluswishlist/', views.plus_wishlist),
    path('minuswishlist/', views.minus_wishlist),
    # path('latest-posts/', latest_posts, name='latest_posts'),
    path('shop/', views.shop, name='shop'),
    path('posts/', views.post_list, name='post_list'),


    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class = MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "nuturemite"
admin.site.site_title = "nuturemite"
admin.site.site_index_title = "welcome to Nuturemite"