from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'todo/task-list.html'
    model = Task
    context_object_name = 'tasks'

    def get_queryset(self):
        base_query = super().get_queryset()
        query = base_query.filter(user=self.request.user)
        return query


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task-list-page')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('task-list-page')
    context_object_name = 'task'


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title']
    template_name = 'todo/task_update_form.html'
    success_url = reverse_lazy('task-list-page')


class TaskDoneView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        task = Task.objects.filter(id=kwargs.get('pk')).first()
        task.is_completed = True
        task.save()
        return redirect(reverse_lazy('task-list-page'))
