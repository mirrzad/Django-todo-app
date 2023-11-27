from django.urls import path
from . import views


urlpatterns = [
    path('task-list/', views.task_list_page, name='task-list-page')
]
