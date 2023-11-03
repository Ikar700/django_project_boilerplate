from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Item


class HomeView(ListView):
    model = Item
    template_name = "home-page.html"


class ProductDetailView(DetailView):
    model = Item
    template_name = "product-page.html"


def checkout(request):
    return render(request, "checkout-page.html")
