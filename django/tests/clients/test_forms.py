from django.core.exceptions import ValidationError
import pytest

from clients.models import Client
from clients.models import Address
from clients.forms import ClientForm


@pytest.mark.django_db
class TestClientForm:
    @pytest.fixture
    def sample_form_data(self):
        return {
            "name": "Jon Doe",
            "phone": "(45) 99999-9999",
            "annotations": "Annotations 1",
            "street": "Street 1",
            "number": "1",
            "neighborhood": "Neighborhood 1",
            "city": "City 1",
        }

    def test_missing_required_fields(self, sample_form_data):
        form = ClientForm(
            data={
                "name": sample_form_data["name"],
            }
        )

        assert form.errors["phone"] == ["This field is required."]
        assert form.errors["street"] == ["This field is required."]
        assert form.errors["number"] == ["This field is required."]
        assert form.errors["neighborhood"] == ["This field is required."]
        assert form.errors["city"] == ["This field is required."]

        assert not form.is_valid()

    def test_invalid_phone(self, sample_form_data):
        sample_form_data["phone"] = "(ab) cdefg-hijk"
        form = ClientForm(data=sample_form_data)

        assert form.errors["phone"] == ["O telefone deve estar no formato (XX) XXXXX-XXXX."]
        assert not form.is_valid()

    def test_invalid_address_fields(self, sample_form_data):
        sample_form_data["number"] = 0
        sample_form_data["street"] = "x" * 101
        sample_form_data["neighborhood"] = "x" * 101
        sample_form_data["city"] = "x" * 101

        form = ClientForm(data=sample_form_data)

        assert form.errors["number"] == ["Ensure this value is greater than or equal to 1."]
        assert form.errors["street"] == ["Ensure this value has at most 100 characters (it has 101)."]
        assert form.errors["neighborhood"] == ["Ensure this value has at most 100 characters (it has 101)."]
        assert form.errors["city"] == ["Ensure this value has at most 100 characters (it has 101)."]
        assert not form.is_valid()

    def test_valid_form_data(self, sample_form_data):
        form = ClientForm(data=sample_form_data)
        assert form.is_valid()

    def test_form_clean_name_raises_validation_error(self, sample_form_data):
        sample_form_data["name"] = ""
        form = ClientForm(data=sample_form_data)
        form.is_valid()

        with pytest.raises(ValidationError):
            form.clean_name()

    def test_form_clean_phone_raises_validation_error(self, sample_form_data):
        sample_form_data["phone"] = ""
        form = ClientForm(data=sample_form_data)

        form.is_valid()
        with pytest.raises(ValidationError):
            form.clean_phone()

    def test_form_save(self, sample_form_data):
        form = ClientForm(data=sample_form_data)
        assert form.is_valid()

        client = form.save()

        assert client.name == "Jon Doe"
        assert client.phone == "(45) 99999-9999"
        assert client.annotations == "Annotations 1"
        assert client.address.street == "Street 1"
        assert client.address.number == 1
        assert client.address.neighborhood == "Neighborhood 1"
        assert client.address.city == "City 1"

    def test_form_with_instace(self):
        address = Address.objects.create(
            street="Street 1",
            number=1,
            neighborhood="Neighborhood 1",
            city="City 1",
        )
        client = Client.objects.create(
            name="Client 1",
            phone="(45) 99999-9999",
            annotations="Annotations 1",
            address=address,
        )
        form = ClientForm(instance=client)

        assert form.fields["street"].initial == "Street 1"
        assert form.fields["number"].initial == 1
        assert form.fields["neighborhood"].initial == "Neighborhood 1"
        assert form.fields["city"].initial == "City 1"
