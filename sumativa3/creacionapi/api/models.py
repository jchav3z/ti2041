from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255)
    rut = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

class Contact(models.Model):
    provider = models.ForeignKey(Provider, related_name='contacts', on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Address(models.Model):
    provider = models.ForeignKey(Provider, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=10)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Service(models.Model):
    provider = models.ForeignKey(Provider, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    thru_date = models.DateField(null=True, blank=True)

# Create your models here.
