from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Task


class TaskListCreateViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("task-list-create")
        self.task_1 = Task.objects.create(
            user=self.user, content="Task 1", completed=False
        )
        self.task_2 = Task.objects.create(
            user=self.user, content="Task 2", completed=True
        )

    def test_create_task(self):
        data = {"content": "Test Task Content"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().content, "Test Task Content")

    def test_list_tasks(self):
        Task.objects.create(user=self.user, content="Task 3")
        Task.objects.create(user=self.user, content="Task 4")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 4)

    def test_completed_filter(self):
        response = self.client.get(self.url, {"completed": "true"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_created_at_gte_filter(self):
        response = self.client.get(
            self.url, {"created_at__gte": "2022-01-01T00:00:00Z"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_created_at_lte_filter(self):
        response = self.client.get(
            self.url, {"created_at__lte": "2022-01-01T00:00:00Z"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_content_contains_filter(self):
        response = self.client.get(self.url, {"content__icontains": "Task"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class TaskViewSetTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(user=self.user, content="Test Task Content")

    def test_mark_as_completed(self):
        url = reverse("tasks-mark-as-completed", args=[self.task.id])
        data = {"task_ids": [self.task.id]}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_mark_as_completed_invalid_task(self):
        url = reverse("tasks-mark-as-completed", args=[999])
        data = {"task_ids": [999]}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
