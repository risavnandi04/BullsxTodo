from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    TaskCreateView,
    TaskRetrieveView,
    TaskListView,
    TaskDeleteView,
    TaskUpdateView,
    MyTokenObtainPairView,
    MyTokenRefreshView,
)


class TestUrls(SimpleTestCase):
    def test_task_create_url(self):
        url = reverse("task_create")
        self.assertEqual(resolve(url).func.view_class, TaskCreateView)

    def test_task_retrieve_url(self):
        url = reverse("task_retrieve", args=["1"])
        self.assertEqual(resolve(url).func.view_class, TaskRetrieveView)

    def test_task_list_url(self):
        url = reverse("task_list")
        self.assertEqual(resolve(url).func.view_class, TaskListView)

    def test_task_update_url(self):
        url = reverse("task_update", args=["1"])
        self.assertEqual(resolve(url).func.view_class, TaskUpdateView)

    def test_task_delete_url(self):
        url = reverse("task_delete", args=["1"])
        self.assertEqual(resolve(url).func.view_class, TaskDeleteView)

    def test_token_obtain_pair_url(self):
        url = reverse("token_obtain_pair")
        self.assertEqual(resolve(url).func.view_class, MyTokenObtainPairView)

    def test_token_refresh_url(self):
        url = reverse("token_refresh")
        self.assertEqual(resolve(url).func.view_class, MyTokenRefreshView)
