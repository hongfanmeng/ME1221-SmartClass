from rest_framework import serializers
from .models import Attendance, AttendanceRecord
from django.utils import timezone


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'title', 'created']
        read_only_fields = ['id', 'created']


class AttendanceDetailSerializer(serializers.ModelSerializer):
    attendanceCount = serializers.SerializerMethodField()
    users = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['id', 'title', 'created', 'attendanceCount', 'users']
        read_only_fields = fields

    def get_users(self, attendance):
        return [record.user.username for record in attendance.attendanceRecords.all()]

    def get_attendanceCount(self, attendance):
        return attendance.attendanceRecords.count()

    def update(self, instance, validated_data):
        user = self.context.get('request').user
        AttendanceRecord.objects.filter(user=user).delete()
        AttendanceRecord.objects.create(user=user, attendance=instance, created=timezone.now())
        return instance


class AttendanceStatusSerializer(serializers.ModelSerializer):
    hasChecked = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = ['hasChecked']

    def get_hasChecked(self, attendance):
        user = self.context.get('request').user
        return attendance.attendanceRecords.filter(user=user).exists()
