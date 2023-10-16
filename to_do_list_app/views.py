from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from to_do_list_app.forms import TaskForm
from to_do_list_app.models import Task


def index(request):
    pass


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    # queryset = Task.objects.all().prefetch_related("")


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("to_do_list_app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("to_do_list_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("to_do_list_app:task-list")


class TagListView(generic.ListView):
    pass


def change_task_status(request, pk):
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("to_do_list_app:task-list"))

