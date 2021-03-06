from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Inprocess', 'Inprocess'),
        ('Prepared', 'Prepared'),
        ('On_the_way', 'On_the_way'),
        ('Delevered', 'Delevered'),
    ]
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS, default="Pending")

    ORDER_SIZE = [
        ('small', 'small'),
        ('medium', 'medium'),
        ('large', 'large'),
        ('extraLarge', 'extraLarge'),
    ]
    size = models.CharField(
        max_length=20, choices=ORDER_SIZE)

    quantity = models.IntegerField()
    toppings = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=10)
    placed_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"< OrderID {self.id} by {self.customer} >"
