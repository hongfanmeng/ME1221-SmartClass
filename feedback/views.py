from rest_framework import generics
from .serializers import FeedbackSerializer
from .models import Feedback
from rest_framework.permissions import IsAdminUser
from utils.permission import IsStudentOrReadOnly
from rest_framework.throttling import UserRateThrottle


class CreateFeedbackThrottle(UserRateThrottle):
    scope = 'createFeedback'


class FeedbackList(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsStudentOrReadOnly | IsAdminUser]

    def get_queryset(self):
        queryset = Feedback.objects.all()
        date = self.request.query_params.get('dateAfter')
        if date is not None:
            queryset = queryset.filter(created__gte=date)
        return queryset

    def get_throttles(self):
        if self.request.method == 'POST' and not self.request.user.is_staff:
            return [CreateFeedbackThrottle()]
        return []
