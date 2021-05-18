from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Attendance(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class AttendanceRecord(models.Model):
    attendance = models.ForeignKey(Attendance, related_name="attendanceRecords", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
