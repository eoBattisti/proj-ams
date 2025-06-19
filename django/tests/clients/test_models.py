from django.core.exceptions import ValidationError
import pytest

from clients.models import Client
from clients.models import Address


@pytest.mark.django_db
class TestAddressModel:
    def test_address_creation(self):
        address = Address.objects.create(
            street="Street 1",
            number=1,
            neighborhood="Neighborhood 1",
            city="City 1",
        )

        assert address.street == "Street 1"
        assert address.number == 1
        assert address.neighborhood == "Neighborhood 1"
        assert address.city == "City 1"

    def test_address_fields_max_length(self):
        long_string = "a" * 200

        with pytest.raises(ValidationError):
            _ = Address.objects.create(
                street=long_string,
                number=1,
                neighborhood="Neighborhood 1",
                city="City 1",
            ).full_clean()

        with pytest.raises(ValidationError):
            _ = Address.objects.create(
                street="Street 1",
                number=1,
                neighborhood=long_string,
                city="City 1",
            ).full_clean()

        with pytest.raises(ValidationError):
            _ = Address.objects.create(
                street="Street 1",
                number=1,
                neighborhood="Neighborhood 1",
                city=long_string,
            ).full_clean()

    def test_address_string_representation(self):
        address = Address.objects.create(
            street="Street 1",
            number=1,
            neighborhood="Neighborhood 1",
            city="City 1",
        )

        assert str(address) == "Street 1, 1, Neighborhood 1 - City 1"


@pytest.mark.django_db
class TestClientModel:
    @pytest.fixture
    def sample_address(self):
        return Address.objects.create(
            street="Street 1",
            number=1,
            neighborhood="Neighborhood 1",
            city="City 1",
        )

    def test_client_creation(self, sample_address):
        client = Client.objects.create(
            name="Client 1",
            phone="(45) 99999-9999",
            annotations="Annotations 1",
            address=sample_address,
        )

        assert client.name == "Client 1"
        assert client.phone == "(45) 99999-9999"
        assert client.annotations == "Annotations 1"
        assert client.address == sample_address

    def test_client_string_representation(self, sample_address):
        client = Client.objects.create(
            name="Client 1",
            phone="(45) 99999-9999",
            annotations="Annotations 1",
            address=sample_address,
        )

        assert str(client) == "Client 1, (45) 99999-9999, Annotations 1 - Street 1, 1, Neighborhood 1 - City 1"
