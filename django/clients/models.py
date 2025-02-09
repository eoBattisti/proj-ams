from core.models import AbstractBaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    street = models.CharField(verbose_name=_("Street"), max_length=100)
    number = models.IntegerField(verbose_name=_("Number"))
    neighborhood = models.CharField(verbose_name=_("Neighborhood"), max_length=100)
    city = models.CharField(verbose_name=_("City"), max_length=100)

    def __str__(self):
        return f"{self.street}, {self.number}, {self.neighborhood} - {self.city}"


class Client(AbstractBaseModel):
    name = models.TextField(verbose_name=_("Name"))
    phone = models.TextField(verbose_name=_("Phone"))
    annotations = models.TextField(verbose_name=_("Annotations"))

    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.annotations} - {self.address}"
