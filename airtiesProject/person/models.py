from django.db import models
from datetime import datetime

# Create your models here.



class person(models.Model): #Our person model
    
    firstName = models.CharField(max_length=50, verbose_name = "Ad", null=True)
    lastName = models.CharField(max_length=50, verbose_name = "Soyad", null=True)
    phone = models.CharField(max_length=50, verbose_name = "Telefon", null=True)
    email = models.EmailField(max_length=100, verbose_name = "Email", null=True)
    createdDate = models.DateField(default = datetime.now, verbose_name = "Oluşturulma Tarihi", null=True)
    
    
    def __str__(self):
        return self.firstName + " " + self.lastName
