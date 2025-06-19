import re

from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Address
from .models import Client


class ClientForm(forms.ModelForm):
    street = forms.CharField(max_length=100, required=True)
    number = forms.IntegerField(required=True, min_value=1)
    neighborhood = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Client
        fields = ["name", "phone", "annotations", "street", "number", "neighborhood", "city"]

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields["number"].label = _("Number")
        self.fields["street"].label = _("Street")
        self.fields["neighborhood"].label = _("Neighborhood")
        self.fields["city"].label = _("City")

        if kwargs.get("instance") is not None:
            self.fields["number"].initial = self.instance.address.number
            self.fields["street"].initial = self.instance.address.street
            self.fields["neighborhood"].initial = self.instance.address.neighborhood
            self.fields["city"].initial = self.instance.address.city

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError('O campo "Nome" não pode estar vazio.')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone:
            raise forms.ValidationError('O campo "Telefone" não pode estar vazio.')

        pattern = r"^\(\d{2}\)\s?\d{4,5}-\d{4}$"

        if not re.match(pattern, phone):
            raise forms.ValidationError("O telefone deve estar no formato (XX) XXXXX-XXXX.")
        return phone

    def save(self, commit=True):
        address = Address.objects.create(
            street=self.cleaned_data["street"],
            number=self.cleaned_data["number"],
            neighborhood=self.cleaned_data["neighborhood"],
            city=self.cleaned_data["city"],
        )

        client = super().save(commit=False)

        client.address = address

        if commit:
            client.save()

        return client
