from django.db import models

from django.utils.translation import gettext_lazy as _

from core.models import AbstractBaseModel


class Sale(AbstractBaseModel):
    client = models.ForeignKey("clients.Client", on_delete=models.PROTECT)
    garment = models.ForeignKey("garments.Garment", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), null=False, blank=False)
    total = models.DecimalField(verbose_name=_("Total"), null=False, blank=False, max_digits=10, decimal_places=2)
    saled_at = models.DateTimeField(verbose_name=_("Saled At"), null=False, blank=False)

    class Meta:
        verbose_name = _("Sale")
        verbose_name_plural = _("Sales")

    def __str__(self):
        return f"{self.client} - {self.garment}"
