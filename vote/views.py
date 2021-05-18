from rest_framework import generics
from .serializers import VoteSerializer, VoteDetailSerializer, VoteStatusSerializer
from .models import Question
from rest_framework.permissions import IsAdminUser
from utils.permission import IsStudentOrReadOnly, IsTeacherOrReadOnly, IsStudent


class VoteList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsTeacherOrReadOnly | IsAdminUser]


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteDetailSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAdminUser()]
        return [(IsStudentOrReadOnly | IsAdminUser)()]


class VoteStatus(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = VoteStatusSerializer
    permission_classes = [IsStudent]
