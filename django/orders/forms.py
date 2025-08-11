from django import forms
from django.forms import ModelForm
from orders.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["client", "discount", "completed", "due_date", "order_date"]
        widgets = {
            "client": forms.Select(attrs={"class": "select select-bordered w-full"}),
            "discount": forms.NumberInput(attrs={"class": "input input-bordered w-full", "value": 0, "min": 0, "max": 100, "step": 1}),
            "completed": forms.CheckboxInput(attrs={"class": "checkbox checkbox-primary"}),
            "due_date": forms.DateInput(attrs={"class": "input input-bordered w-full", "type": "date", "format": "%Y-%m-%d"}),
            "order_date": forms.DateInput(attrs={"class": "input input-bordered w-full", "type": "date", "format": "%Y-%m-%d"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if kwargs.get("instance") is not None:
            self.initial["order_date"] = self.instance.order_date.strftime("%Y-%m-%d")
            self.initial["due_date"] = self.instance.due_date.strftime("%Y-%m-%d")
