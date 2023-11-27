from django.shortcuts import render


def task_list_page(request):
    return render(request, 'todo/task-list.html')
