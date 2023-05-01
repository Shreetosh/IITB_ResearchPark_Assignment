from django.db import models
from jsonfield import JSONField

# Create your models here.
class Invoice(models.Model):
    invoice_no = models.CharField(max_length=255, null=True)
    date_time = models.CharField(max_length=255, null=True)
    customer_name = models.CharField(max_length=255, null=True)
    customer_phone = models.CharField(max_length=10, null=True)
    customer_email = models.CharField(max_length=100, null=True)
    items = JSONField(null = True)
    prices = JSONField(null = True)
    quantities = JSONField(null = True)
    tax = JSONField(null=True)
    amount = JSONField(null=True)
