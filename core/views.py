from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect
from django.utils import timezone
from .models import Item, OrderItem, Order


class HomeView(ListView):
    model = Item
    template_name = "home-page.html"


class ProductDetailView(DetailView):
    model = Item
    template_name = "product-page.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user = request.user,
        ordered=False 
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists:
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, 
                                     ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product-page", slug= slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists:
            order_item = OrderItem.objects.filter(
                item=item,
                user = request.user,
                ordered=False 
            )[0]
            order.items.remove(order_item)
        else:
            return redirect("core:product-page", slug=slug)
    else:
        return redirect("core:product-page", slug=slug)
    return redirect("core:product-page", slug=slug)


def checkout(request):
    return render(request, "checkout-page.html")
