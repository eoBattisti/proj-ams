from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from core.models import AbstractBaseModel


class Material(AbstractBaseModel):
    description = models.TextField(verbose_name=_("Description"), null=False, blank=False)
    value = models.DecimalField(
        verbose_name=_("Value"),
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(limit_value=0, message=_("Material value must be greater than 0"))],
    )

    class Meta:
        verbose_name = _("Material")
        verbose_name_plural = _("Materials")
        ordering = ("value",)

    def __str__(self) -> str:
        """Returns a string representation of the material"""
        return f"{self.description}"


class Garment(AbstractBaseModel):
    class GarmentSize(models.IntegerChoices):
        SMALL = 1, _("Small")
        MEDIUM = 2, _("Medium")
        LARGE = 3, _("Large")
        EXTRA_LARGE = 4, _("Extra Large")

    name = models.CharField(verbose_name=_("Name"), max_length=255, null=False, blank=False)
    size = models.PositiveSmallIntegerField(verbose_name=_("Size"), null=False, blank=False, choices=GarmentSize)
    value = models.DecimalField(
        verbose_name=_("Value"),
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(limit_value=0, message=_("Garment value must be greater than 0"))],
    )
    description = models.TextField(verbose_name=_("Description"), null=False, blank=False)
    materials = models.ManyToManyField(verbose_name=_("Materials"), to=Material, related_name="garments")

    class Meta:
        verbose_name = _("Garment")
        verbose_name_plural = _("Garments")
        ordering = ("name",)

    def __str__(self) -> str:
        """Returns a string representation of the garment"""
        return f"{self.name} - {self.size}"

    @property
    def profit(self) -> Decimal:
        """Returns the profit of the garment"""
        return Decimal(value=(self.value - self.total_cost))

    @property
    def total_cost(self) -> Decimal:
        """Returns the total cost of the garment"""
        return Decimal(value=sum([material.value for material in self.materials.all()]))
