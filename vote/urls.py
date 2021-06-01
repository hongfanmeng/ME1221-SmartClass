from django.urls import path
from .views import VoteList, VoteDetail, VoteStatus
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('votes/', VoteList.as_view()),
    path('votes/<int:pk>/', VoteDetail.as_view()),
    path('votes/<int:pk>/status', VoteStatus.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
