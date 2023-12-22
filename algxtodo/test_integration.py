from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Task
from datetime import timedelta
from django.utils import timezone


class IntegrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(
            title="Task 1",
            description="Task 1 description",
            due_date=timezone.now() + timedelta(days=5),
            status="OPEN",
        )
        self.task2 = Task.objects.create(
            title="Task 2",
            description="Task 2 description",
            due_date=timezone.now() + timedelta(days=10),
            status="WORKING",
        )

    def test_task_create(self):
        # Test creating a new task
        response = self.client.post(
            reverse("task_create"),
            {
                "title": "Task 3",
                "description": "Task 3 description",
                "due_date": (timezone.now() + timedelta(days=7)).strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
                "status": "OPEN",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_task_retrieve(self):
        # Test retrieving a task
        response = self.client.get(
            reverse("task_retrieve", kwargs={"pk": self.task1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data,
            {
                "id": 1,
                "title": "Task 1",
                "description": "Task 1 description",
                "due_date": self.task1.due_date.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                )
                if self.task1.due_date
                else None,
                "status": "OPEN",
                "tags": list(self.task1.tags.values_list('name', flat=True)),
                "timestamp": self.task1.timestamp.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
            },
        )

    def test_task_list(self):
        # Test listing all tasks
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_task_update(self):
        # Test updating a task
        response = self.client.put(
            reverse("task_update", kwargs={"pk": self.task1.pk}),
            {
                "title": "Task 1 updated",
                "description": "Task 1 description updated",
                "due_date": (timezone.now() + timedelta(days=5)).strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
                "status": "DONE",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_task_delete(self):
        # Test deleting a task
        response = self.client.delete(
            reverse("task_delete", kwargs={"pk": self.task1.pk})
        )
        self.assertEqual(response.status_code, 204)
