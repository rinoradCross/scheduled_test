from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Schedule


class ScheduleAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.schedule_data = {
            "day": "monday",
            "start": "09:00",
            "stop": "17:00",
            "ids": [1, 2, 3],
        }
        self.url = "/api/schedules/"

    def test_create_schedule(self):
        response = self.client.post(self.url, self.schedule_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Schedule.objects.count(), 1)
        self.assertEqual(Schedule.objects.get().day, "monday")

    def test_get_schedule_list(self):
        Schedule.objects.create(**self.schedule_data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
