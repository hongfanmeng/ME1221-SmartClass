from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth.models import Group


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return Group.objects.get(name="teacher").user_set.filter(id=user.id).exists()


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return Group.objects.get(name="student").user_set.filter(id=user.id).exists()


class IsStudentOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return Group.objects.get(name="student").user_set.filter(id=user.id).exists()


class IsTeacherOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return Group.objects.get(name="teacher").user_set.filter(id=user.id).exists()
