from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Category(models.Model):
    # Category name with a unique constraint
    name = models.CharField(max_length=50, unique=True)
    # Optional description for the category
    description = models.TextField(null=True, blank=True)
    # Optionally, associate a user with the category
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=12, 
        choices=STATUS_CHOICES, 
        default='PENDING'
    )
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], 
        null=True, 
        blank=True
    )
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Optionally, associate a user with the task
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    # Optionally, associate a user with the comment
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment on {self.task.title} by {self.user.username if self.user else 'Anonymous'}"
