import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def create_sample_user(api_client):
    url = reverse('api-register')
    data = {
        'username': 'test',
        'password': 'a@123456789',
        'password1': 'a@123456789',
    }
    return api_client.post(url, data)


@pytest.mark.django_db
class TestAccountApi:
    def test_account_register(self, api_client, create_sample_user):
        response = create_sample_user
        user = User.objects.get(username=response.data.get('username'))
        assert response.status_code == 201
        assert response.data.get('username') == user.username

    def test_account_token_login(self, api_client, create_sample_user):
        create_sample_user
        url_login = reverse('api-login-token')
        data_login = {
            'username': 'test',
            'password': 'a@123456789'
        }

        response = api_client.post(url_login, data_login)
        user = User.objects.get(pk=response.data.get('user_id'))
        assert response.status_code == 200
        assert response.data.get('token') == str(user.auth_token)

    def test_account_jwt_login(self, api_client, create_sample_user):
        create_sample_user
        url_login = reverse('jwt_obtain_pair')
        data_login = {
            'username': 'test',
            'password': 'a@123456789',
        }
        response = api_client.post(url_login, data_login)
        assert response.status_code == 200
