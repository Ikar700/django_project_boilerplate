from django.urls import path
from .views import HomeView, checkout, ProductDetailView, add_to_cart, remove_from_cart


app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('checkout/', checkout, name="checkout-page"),
    path('product/<slug>/', ProductDetailView.as_view(), name="product-page"),
    path('add-to-cart/<slug>/', add_to_cart, name="add-to-cart" ),
    path('remove-from-cart/<slug>/', remove_from_cart, name="remove-from-cart")
]
