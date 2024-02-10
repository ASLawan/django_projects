from django.test import TestCase
from .models import Task
# Create your tests here.

class TaskModelTest(TestCase):
    def test_task_model_exists(self):
        """Test if the model exists"""
        tasks = Task.objects.count()

        self.assertEqual(tasks, 0)