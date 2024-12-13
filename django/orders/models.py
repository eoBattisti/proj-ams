from django.db import models

from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from core.models import AbstractBaseModel


class OrderType(AbstractBaseModel):
    description = models.CharField(verbose_name=_("Description"), max_length=255, null=False, blank=False)
    base_value = models.DecimalField(
        verbose_name=_("Value"),
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        validators=[MinValueValidator(limit_value=0, message=_("The Base Value must be greater than 0"))],
    )

    class Meta:
        verbose_name = _("Order Type")
        verbose_name_plural = _("Order Types")
        ordering = ("description",)

    def __str__(self):
        return f"{self.description} - {self.base_value}"


class Order(AbstractBaseModel):
    description = models.CharField(verbose_name=_("Description"), max_length=255, null=False, blank=False)
    value = models.DecimalField(
        verbose_name=_("Value"),
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=True,
        validators=[MinValueValidator(limit_value=0, message=_("The Value must be greater than 0"))],
    )

    order_type = models.ForeignKey(
        verbose_name=_("Order Type"), to=OrderType, on_delete=models.CASCADE, related_name="orders"
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ("description",)

    def __str__(self):
        return f"{self.description} - {self.value}"
