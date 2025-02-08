from django import forms
from django.forms import ModelForm
from orders.models import Order


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ["client", "discount", "completed", "due_date", "order_date"]
        widgets = {
            "client": forms.Select(attrs={"class": "form-select"}),
            "discount": forms.NumberInput(attrs={"class": "form-control", "value": 0, "min": 0, "max": 100, "step": 1}),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input", "for": "completed"}),
            "due_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "format": "%d/%m/%Y"}),
            "order_date": forms.DateInput(attrs={"class": "form-control", "type": "date", "format": "%d/%m/%Y"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs.get("instance") is not None:
            self.initial["order_date"] = self.instance.order_date.strftime("%Y-%m-%d")
            self.initial["due_date"] = self.instance.due_date.strftime("%Y-%m-%d")

