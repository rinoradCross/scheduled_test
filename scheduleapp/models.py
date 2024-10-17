from django.db import models


class Schedule(models.Model):
    day_choices = [
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ]
    day = models.CharField(max_length=10, choices=day_choices)
    start = models.TimeField()
    stop = models.TimeField()
    ids = models.JSONField()
