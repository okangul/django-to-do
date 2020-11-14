from django.db import models
from django_extensions.db.models import TimeStampedModel


class Task(TimeStampedModel):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

