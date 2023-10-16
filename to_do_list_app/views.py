from django.shortcuts import render
from django.views import generic

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


class TaskUpdateView(generic.UpdateView):
    pass


class TaskDeleteView(generic.DeleteView):
    pass


class TagListView(generic.ListView):
    pass


def change_task_status():
    pass

