from django.urls import path
from .views import HomeView, checkout, ProductDetailView


app_name = 'core'


urlpatterns = [
    path('', HomeView.as_view(), name="home-page"),
    path('checkout/', checkout, name="checkout-page"),
    path('product/<slug>/', ProductDetailView.as_view(), name="product-page")
]
