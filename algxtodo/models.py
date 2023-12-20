from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "OPEN"),
        ("WORKING", "WORKING"),
        ("DONE", "DONE"),
        ("OVERDUE", "OVERDUE"),
    ]
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=7, choices=STATUS_CHOICES, default="OPEN"
    )

    def clean(self):
        super().clean()

        # Check if due_date is before timestamp
        self.timestamp= timezone.now()
        if self.due_date < self.timestamp:
            print("Parameteres In model file")
            print(self.due_date)
            print(self.timestamp)
            print(self.due_date < self.timestamp)
            raise ValidationError("Due date cannot be before the timestamp.")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
