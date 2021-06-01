from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FeedbackList

urlpatterns = [
    path('feedbacks/', FeedbackList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
