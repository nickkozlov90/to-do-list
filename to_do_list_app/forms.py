from django import forms

from to_do_list_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "is_done",
            "tags"
        ]