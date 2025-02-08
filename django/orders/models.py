from core.models import AbstractBaseModel
from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from tasks.models import Task


class Order(AbstractBaseModel):
    client = models.ForeignKey(verbose_name=_("Client"), to="clients.Client", on_delete=models.CASCADE)
    discount = models.FloatField(verbose_name=_("Discount"), null=True, blank=True)
    completed = models.BooleanField(verbose_name=_("Completed"), default=False)
    tasks = models.ManyToManyField(verbose_name=_("Services"), to="tasks.Task")
    due_date = models.DateField(verbose_name=_("Due Date"), null=True, blank=True)
    order_date = models.DateField(verbose_name=_("Order Date"), null=True, blank=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    @property
    def total(self):
        tasks: QuerySet[Task, Task] = self.tasks.all()
        return sum([task.value for task in tasks])
