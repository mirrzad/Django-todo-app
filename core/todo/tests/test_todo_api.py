import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from todo.models import Task


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def sample_user():
    user = User.objects.create(username='test', password='a@123456789')
    return user


@pytest.fixture
def sample_todo_obj(sample_user):
    todo = Task.objects.create(
        title='test',
        user=sample_user
    )
    return todo


@pytest.mark.django_db
class TestTodoApi:

    def test_get_todo_list(self, sample_user, api_client):
        api_client.force_authenticate(user=sample_user)
        url = reverse('tasks-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_get_todo_list_without_auth(self, api_client):
        url = reverse('tasks-list')
        response = api_client.get(url)
        assert response.status_code == 401

    def test_create_todo_item(self, sample_user, api_client):
        api_client.force_authenticate(user=sample_user)
        url = reverse('tasks-list')
        data = {
            'title': 'test',
            'is_completed': True
        }
        response = api_client.post(url, data)
        assert response.status_code == 201
        assert Task.objects.get(pk=response.data.get('id')).id == response.data.get('id')

    def test_create_todo_item_without_auth(self, api_client):
        url = reverse('tasks-list')
        data = {
            'title': 'test',
            'is_completed': True
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_get_todo_item(self, sample_user, api_client, sample_todo_obj):
        api_client.force_authenticate(user=sample_user)
        url = reverse('tasks-detail', kwargs={'pk': sample_todo_obj.id})
        response = api_client.get(url)
        assert response.status_code == 200

    def test_update_todo_item(self, sample_user, api_client, sample_todo_obj):
        api_client.force_authenticate(user=sample_user)
        url = reverse('tasks-detail', kwargs={'pk': sample_todo_obj.id})
        data = {
            'title': 'test_edited',
            'is_completed': True
        }
        response = api_client.put(url, data)
        assert response.status_code == 200

    def test_update_partial_todo_item(self, sample_user, api_client, sample_todo_obj):
        api_client.force_authenticate(user=sample_user)
        url = reverse('tasks-detail', kwargs={'pk': sample_todo_obj.id})
        data = {
            'is_completed': True
        }
        response = api_client.patch(url, data)
        assert response.status_code == 200

    def test_delete_todo_item(self, sample_user, api_client, sample_todo_obj):
        api_client.force_authenticate(user=sample_user)
        url = reverse('tasks-detail', kwargs={'pk': sample_todo_obj.id})
        response = api_client.delete(url)
        assert response.status_code == 204
