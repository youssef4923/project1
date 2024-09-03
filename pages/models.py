from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.name
