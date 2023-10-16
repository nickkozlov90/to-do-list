from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created"]

    def __str__(self):
        return f"{self.content}"

    def get_queryset(self):
        return Task.objects.prefetch_related('tags')
