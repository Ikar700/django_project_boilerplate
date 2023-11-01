from django.conf import settings
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now=True)
    ordered_date = models.DateTimeField

    def __str__(self):
        return self.name
