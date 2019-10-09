from django.db import models

# Create your models here.
class customerBooking(models.Model):
    customer_name = models.TextField()
    email = models.TextField()

