from django.db import models


from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

from core.models import AbstractBaseModel


class TaskType(AbstractBaseModel):
    description = models.CharField(verbose_name =_("Description"), max_length=255, null=False, blank=False)
    base_value = models.DecimalField(
        verbose_name=_("Base Value"),
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=True,
        validators=[MinValueValidator(limit_value=0, message=_("The Value must be greater than 0"))],
    )

    class Meta:
        verbose_name = _("Task Type")
        verbose_name_plural = _("Task Types")
        ordering = ("description",)

    def __str__(self):
        return f"{self.description} - {self.base_value}"


class Task(AbstractBaseModel):
    description = models.CharField(verbose_name=_("Description"), max_length=255, null=False, blank=False)
    value = models.DecimalField(
        verbose_name=_("Value"),
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=True,
        validators=[MinValueValidator(limit_value=0, message=_("The Value must be greater than 0"))],
    )

    task_type = models.ForeignKey(
        verbose_name=_("Task Type"), to=TaskType, on_delete=models.CASCADE, related_name="Task_Type"
    )

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")
        ordering = ("description",)

    def __str__(self):
        return f"{self.description} - {self.value}"
