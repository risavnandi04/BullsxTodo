from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

def validate_due_date(value):
    if value < timezone.now():
        raise ValidationError("The due date must be after the current time.")

class Task(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "OPEN"),
        ("WORKING", "WORKING"),
        ("DONE", "DONE"),
        ("OVERDUE", "OVERDUE"),
    ]
    # breakpoint()
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(
        null=True, blank=True, validators=[validate_due_date]
    )
    tags = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default="OPEN"
    )

    def __str__(self):
        return self.title
