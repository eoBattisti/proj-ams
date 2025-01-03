from django.forms import ModelForm, DecimalField

from garments.models import Garment, Material


class GarmentForm(ModelForm):
    value = DecimalField(min_value=0, max_digits=10, decimal_places=2, initial=0)

    class Meta:
        model = Garment
        fields = ["name", "size", "value", "description", "materials"]


class MaterialForm(ModelForm):
    value = DecimalField(min_value=0, max_digits=10, decimal_places=2, initial=0)

    class Meta:
        model = Material
        fields = ["description", "value"]
