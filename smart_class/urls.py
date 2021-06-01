from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from attendance.views import AttendanceList, AttendanceDetail, AttendanceStatus
from vote.views import VoteList, VoteDetail, VoteStatus
from feedback.views import FeedbackList
from utils.views import AuthToken
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', AuthToken.as_view()),
    path('votes/', VoteList.as_view()),
    path('votes/<int:pk>/', VoteDetail.as_view()),
    path('votes/<int:pk>/status/', VoteStatus.as_view()),
    path('attendances/', AttendanceList.as_view()),
    path('attendances/<int:pk>/', AttendanceDetail.as_view()),
    path('attendances/<int:pk>/status/', AttendanceStatus.as_view()),
    path('feedbacks/', FeedbackList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
