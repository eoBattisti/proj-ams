from decimal import Decimal

from django.forms import DecimalField, ModelForm

from orders.models import Order, OrderType


class OrderForm(ModelForm):
    value = DecimalField(min_value=0, max_digits=10, decimal_places=2, initial=0)

    class Meta:
        model = Order
        fields = ["description", "value", "order_type"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance: Order

    def clean(self):
        cleaned_data = super().clean()

        value: Decimal = cleaned_data.get("value")
        order_type: OrderType = cleaned_data.get("order_type")

        # We validate if the value for the Order is not provided,
        # we set it to the base value of the OrderType
        if value == 0 and order_type:
            cleaned_data["value"] = order_type.base_value

        return cleaned_data


class OrderTypeForm(ModelForm):
    base_value = DecimalField(min_value=0, max_digits=10, decimal_places=2, initial=0)

    class Meta:
        model = OrderType
        fields = ["description", "base_value"]
