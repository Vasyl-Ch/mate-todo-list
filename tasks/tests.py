from django.urls import reverse
from django.test import TestCase

from tasks.models import Task


class TaskListViewTests(TestCase):
    def test_no_tasks(self):
        response = self.client.get(reverse("tasks:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You don't have any tasks yet")

    def test_task_in_list(self):
        task = Task.objects.create(content="Test task")
        response = self.client.get(reverse("tasks:home"))
        self.assertContains(response, task.content)
