from django.test import TestCase
# from django.db.utils import DataError, IntegrityError
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Task, Tag
from django.db.models import Manager

class TestTaskModel(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            status="OPEN",
            due_date=timezone.now()
            + timezone.timedelta(
                days=1
            ),  # due_date is 1 day after the current date
        )
        tag1 = Tag.objects.create(name="test")
        tag2 = Tag.objects.create(name="django")
        self.task.tags.set([tag1, tag2])

    def test_task_fields(self):
        self.assertIsInstance(self.task.title, str)
        self.assertIsInstance(self.task.description, str)
        self.assertIsInstance(self.task.status, str)
        self.assertIn(self.task.status, dict(Task.STATUS_CHOICES))
        self.assertTrue(len(self.task.title) <= 200)
        self.assertTrue(len(self.task.description) <= 1000)

    def test_str_method(self):
        self.assertEqual(str(self.task), self.task.title)

    # Negative test case
    # def test_long_title(self):
    #     long_title = "a" * 201  # 200 is the max_length
    #     task = Task(title=long_title, description="Test", status="OPEN")
    #     with self.assertRaises(DataError):
    #         task.full_clean()
    #         task.save()

    def test_default_status(self):
        self.assertEqual(self.task.status, "OPEN")

    # Negative test case
    # def test_invalid_status(self):
    #     self.task.status = "INVALID"
    #     with self.assertRaises(ValueError):
    #         self.task.full_clean()
    #         self.task.save()

    # Negative test case
    # def test_null_title(self):
    #     task = Task(description="Test", status="OPEN")
    #     with self.assertRaises(IntegrityError):
    #         task.full_clean()
    #         task.save()

    def test_due_date_field(self):
        self.assertIsInstance(self.task.due_date, timezone.datetime)
        self.assertTrue(self.task.due_date > self.task.timestamp)

    def test_timestamp_field(self):
        self.assertIsInstance(self.task.timestamp, timezone.datetime)

    def test_tags_field(self):
        self.assertIsInstance(self.task.tags, Manager)

    def test_due_date_after_timestamp(self):
        # Set the timestamp to the current date and time
        self.task.timestamp = timezone.now()

        # Set the due_date to be 1 day after the timestamp
        self.task.due_date = self.task.timestamp + timezone.timedelta(days=1)

        # Check if due_date is after timestamp
        self.assertTrue(self.task.due_date > self.task.timestamp)

        # Try to save the task
        try:
            self.task.full_clean()
            self.task.save()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly!")

        # Set the due_date to be 1 day before the timestamp
        self.task.due_date = self.task.timestamp - timezone.timedelta(days=1)
        print(self.task.due_date)
        print(self.task.timestamp)

        # Check if due_date is before timestamp
        with self.assertRaises(ValidationError):
            self.task.full_clean()
            # self.task.save()
