from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("contact/", views.contact_view, name="contact"),
    path("checkout/", views.checkout_view, name="checkout"),
    path("cart/", views.cart_view, name="cart"),
]