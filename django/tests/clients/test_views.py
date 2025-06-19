import pytest

from django.urls import reverse

from clients.models import Address
from clients.models import Client


@pytest.mark.django_db
class TestClientsViews:
    @pytest.fixture
    def sample_client(self):
        address = Address.objects.create(
            street="Street 1",
            number=1,
            neighborhood="Neighborhood 1",
            city="City 1",
        )
        return Client.objects.create(
            name="Client 1", phone="(45) 99999-9999", annotations="Annotations 1", address=address
        )

    def test_unauthenticated_user_access_list_clients_view(self, client):
        response = client.get(reverse("clients:list"))

        assert response.status_code == 302
        assert reverse("login") in response.url

    def test_unauthenticated_user_access_create_clients_view(self, client):
        response = client.get(reverse("clients:create"))

        assert response.status_code == 302
        assert reverse("login") in response.url

    def test_unauthenticated_user_access_update_clients_view(self, client, sample_client):
        response = client.get(reverse("clients:update", args=[sample_client.id]))

        assert response.status_code == 302
        assert reverse("login") in response.url

    def test_unauthenticated_user_access_detail_clients_view(self, client, sample_client):
        response = client.get(reverse("clients:detail", args=[sample_client.id]))

        assert response.status_code == 302
        assert reverse("login") in response.url

    def test_authenticated_user_access_list_clients_view(self, authenticated_client):
        response = authenticated_client.get(reverse("clients:list"))
        assert response.status_code == 200

    def test_authenticated_user_access_create_clients_view(self, authenticated_client):
        response = authenticated_client.get(reverse("clients:create"))
        assert response.status_code == 200

    def test_authenticated_user_access_update_clients_view(self, authenticated_client, sample_client):
        response = authenticated_client.get(reverse("clients:update", args=[sample_client.id]))
        assert response.status_code == 200

    def test_authenticated_user_access_detail_clients_view(self, authenticated_client, sample_client):
        response = authenticated_client.get(reverse("clients:detail", args=[sample_client.id]))
        assert response.status_code == 200

    def test_create_client_view_with_htmx_headers(self, authenticated_client):
        data = {
            "name": "Client 1",
            "phone": "(45) 99999-9999",
            "annotations": "Annotations 1",
            "street": "Street 1",
            "number": 1,
            "neighborhood": "Neighborhood 1",
            "city": "City 1",
        }
        headers = {
            "HX-Request": "true",
        }
        response = authenticated_client.post(reverse("clients:create"), data=data, headers=headers)
        assert response.status_code == 200
