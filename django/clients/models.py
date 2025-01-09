from django.db import models
from core.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    street = models.CharField(verbose_name=_("Rua"), max_length=100)
    number = models.IntegerField(verbose_name=_("Numero"))
    neighborhood = models.CharField(verbose_name=_("Bairro"), max_length=100)
    city = models.CharField(verbose_name=_("Cidade"), max_length=100)

    def __str__(self):
        return f"{self.street}, {self.number}, {self.neighborhood} - {self.city}"


class Client(AbstractBaseModel):
    name = models.TextField(verbose_name=_("Nome"))
    phone = models.TextField(verbose_name=_("Telefone"))
    annotations = models.TextField(verbose_name=_("Anotações"))

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.annotations} - {self.address}"
