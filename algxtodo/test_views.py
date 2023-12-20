from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.views import status
from .models import Task
from .serializer import TaskSerializer

# initialize the APIClient app
client = APIClient()


class TaskTest(TestCase):
    """Test module for Task model"""

    def setUp(self):
        self.task1 = Task.objects.create(
            title="Task 1", description="Task 1 description"
        )
        self.task2 = Task.objects.create(
            title="Task 2", description="Task 2 description"
        )

    def test_get_all_tasks(self):
        # get API response
        response = client.get(reverse("task_list"))
        # get data from db
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task(self):
        # get API response
        response = client.get(
            reverse("task_retrieve", kwargs={"pk": self.task1.pk})
        )
        # get data from db
        task = Task.objects.get(pk=self.task1.pk)
        serializer = TaskSerializer(task)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        # prepare data
        data = {"title": "Task 3", "description": "Task 3 description"}
        # post API response
        response = client.post(reverse("task_create"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        # prepare data
        data = {
            "title": "Task 1 updated",
            "description": "Task 1 description updated",
        }
        # put API response
        response = client.put(
            reverse("task_update", kwargs={"pk": self.task1.pk}), data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        # delete API response
        response = client.delete(
            reverse("task_delete", kwargs={"pk": self.task1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
