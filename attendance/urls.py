from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AttendanceList, AttendanceDetail, AttendanceStatus

urlpatterns = [
    path('attendances/', AttendanceList.as_view()),
    path('attendances/<int:pk>/', AttendanceDetail.as_view()),
    path('attendances/<int:pk>/status/', AttendanceStatus.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
