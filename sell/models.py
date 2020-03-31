from django.db import models
from django.conf import settings
from djrichtextfield.models import RichTextField

class Policy(models.Model):
    content = RichTextField()
class Term(models.Model):
    content = RichTextField()
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    quote = models.CharField(max_length=250)
    image = models.ImageField(upload_to="customer/", default='..{}img/customer/customer-1.png'.format(settings.STATIC_URL))
class Trip(models.Model):
    trip_link = models.URLField(
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
