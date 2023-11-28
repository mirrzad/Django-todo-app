from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list-page'),
    path('create-task/', views.CreateTaskView.as_view(), name='create-task-page'),
    path('delete-task/<int:pk>/', views.DeleteTaskView.as_view(), name='delete-task-page'),
    path('update-task/<int:pk>/', views.UpdateTaskView.as_view(), name='update-task-page'),
    path('task-done/<int:pk>/', views.TaskDoneView.as_view(), name='task-done-action'),
]
