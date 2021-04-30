from smartclass.smartclassroom.models import Question, Feedback
from smartclass.smartclassroom.serializers import VoteSerializer, FeedbackSerializer, VoteDetailSerializer
from rest_framework import generics


class VoteList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteSerializer


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteDetailSerializer


class FeedbackList(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
