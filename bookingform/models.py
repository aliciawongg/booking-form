from django.db import models

# Create your models here.
class customerBooking(models.Model):
    customer_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact_num = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    service = models.CharField(max_length=50)

