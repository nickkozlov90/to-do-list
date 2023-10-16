from django.urls import path

from .views import (
    index, TaskListView, TagListView, TaskCreateView, TaskUpdateView, TaskDeleteView, change_task_status
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/change-task-status/",
        change_task_status,
        name="change-task-status"
    ),

]

app_name = "to_do_list_app"
