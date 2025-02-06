import re

from django import forms

from .models import Address
from .models import Client


class ClientForm(forms.ModelForm):
    # Campos de endereço adicionados ao formulário
    street = forms.CharField(max_length=100, required=True)
    number = forms.IntegerField(required=True)
    neighborhood = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)

    class Meta:
        model = Client
        fields = ["name", "phone", "annotations", "street", "number", "neighborhood", "city" ]
        widgets = {
                "name": forms.TextInput(attrs={"class": "form-control", "autofocus": True}),
                "phone": forms.TextInput(attrs={"class": "form-control"}),
                "annotations": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields["number"].widget.attrs["class"] = "form-control"
        self.fields["street"].widget.attrs["class"] = "form-control"
        self.fields["neighborhood"].widget.attrs["class"] = "form-control"
        self.fields["city"].widget.attrs["class"] = "form-control"

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

    def clean_number(self):
        number = self.cleaned_data.get("number")
        if number <= 0:
            raise forms.ValidationError("O numero deve ser diferente de 0")
        return number

    def clean_street(self):
        street = self.cleaned_data.get("street")
        if not street:
            raise forms.ValidationError('O campo "Rua" não pode estar vazio.')
        return street

    def clean_neighborhood(self):
        neighborhood = self.cleaned_data.get("neighborhood")
        if not neighborhood:
            raise forms.ValidationError('O campo "Bairro" não pode estar vazio.')
        return neighborhood

    def clean_city(self):
        city = self.cleaned_data.get("city")
        if not city:
            raise forms.ValidationError('O campo "Cidade" não pode estar vazio.')
        return city

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
