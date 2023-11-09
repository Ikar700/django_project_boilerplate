from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.db import models

CATEGORY_CHOICES = (("S", "Shirt"), ("Sw", "SportWear"), ("OW", "Outwear"))


LABEL_CHOICES = (
    ("P", "primary"),
    ("S", "secondary"),
    ("D", "danger"),
)


class Item(models.Model):
    name = models.CharField(max_length=100)
    normal_price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:product-page", kwargs={
            "slug": self.slug
        }
        )
    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            "slug": self.slug
        })
    
    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            "slug": self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField(timezone.now())
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

