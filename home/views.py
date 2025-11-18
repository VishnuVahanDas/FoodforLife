from django.shortcuts import render


# Create your views here.
def home_view(request):
    return render(request, "index.html")


def contact_view(request):
    return render(request, "contact.html")


def cart_view(request):
    return render(request, "cart.html")


def checkout_view(request):
    return render(request, "checkout.html")


def donation_checkout_view(request):
    return render(request, "donation_checkout.html")
