from django.db import models
from django.core.validators import MaxLengthValidator
# Create your models here.

class employee(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_number = models.EmailField(max_length=150)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(validators=[MaxLengthValidator(10)],max_length=10)
    job_title = models.CharField(max_length=150)
    descr = models.TextField(max_length=500)
    

