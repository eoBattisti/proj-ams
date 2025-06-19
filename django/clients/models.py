from core.models import AbstractBaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator
from django.core.validators import RegexValidator


class Address(models.Model):
    street = models.CharField(
        verbose_name=_("Street"),
        max_length=100,
        validators=[MaxLengthValidator(100)]
    )
    number = models.IntegerField(
        verbose_name=_("Number")
    )
    neighborhood = models.CharField(
        verbose_name=_("Neighborhood"),
        max_length=100,
        validators=[MaxLengthValidator(100)]
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=100,
        validators=[MaxLengthValidator(100)]
    )

    def __str__(self):
        return f"{self.street}, {self.number}, {self.neighborhood} - {self.city}"


class Client(AbstractBaseModel):
    name = models.TextField(
        verbose_name=_("Name"),
        blank=False
    )
    phone = models.TextField(verbose_name=_("Phone"))
    annotations = models.TextField(
        verbose_name=_("Annotations"),
        blank=True
    )

    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.annotations} - {self.address}"
