from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Pizzas(models.Model):
    name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zip_code = models.IntegerField(max_length=20, blank=True, default=0)
    website =models.URLField(max_length=200, blank=True)
    phone_number = models.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],#+
        max_length=17,#+
        blank=True,#+
        null=True,#+
        help_text='Format: +999999999'#+
    )


    description = models.TextField(blank=True)
    logo_image = models.ImageField(
        blank=True,
        upload_to='Images/logo.png'
    )
     
     
    email = models.EmailField(max_length=254, blank=True) 
    active = models.BooleanField(default=True)  

    def __str__(self):
        return f"{self.name}, {self.city}"