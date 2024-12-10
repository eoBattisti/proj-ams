from django.db import models
from core.models import AbstractBaseModel

class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.street}, {self.number}, {self.neighborhood} - {self.city}"
    
class Client(AbstractBaseModel):
    name = models.TextField()
    phone = models.TextField()
    annotations = models.TextField()
    
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}, {self.phone}, {self.annotations} - {self.address}"
