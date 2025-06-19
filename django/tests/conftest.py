import pytest

from django.contrib.auth.models import User

@pytest.fixture(scope="function")
def user(db):
    return User.objects.create_user(username="admin", email="admin@admin.com", password="admin")


@pytest.fixture(scope="function")
def authenticated_client(client, user):
    client.force_login(user)
    return client
