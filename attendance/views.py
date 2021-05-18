from .models import Attendance
from .serializers import AttendanceSerializer, AttendanceDetailSerializer, AttendanceStatusSerializer
from utils.permission import IsStudent, IsTeacher
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher | IsAdminUser]


class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceDetailSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        elif self.request.method == 'PUT':
            return [IsStudent()]
        return [(IsTeacher | IsAdminUser)()]


class AttendanceStatus(generics.RetrieveAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceStatusSerializer
    permission_classes = [IsStudent]
