from smartclass.smartclassroom.models import Question, Feedback
from smartclass.smartclassroom.serializers import VoteSerializer, FeedbackSerializer, VoteDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class VoteList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteSerializer


class VoteDetail(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteDetailSerializer


class CreateVote(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]


class UpdateVote(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteDetailSerializer
    permission_classes = [IsAuthenticated]


class FeedbackList(generics.ListAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        queryset = Feedback.objects.all()
        date = self.request.query_params.get('date')

        if date is not None:
            queryset = queryset.filter(created__gte=date)
        return queryset


class CreateFeedback(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    throttle_scope = 'createFeedback'
