from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class CustomUser(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    
    def __str__(self):
        return self.email