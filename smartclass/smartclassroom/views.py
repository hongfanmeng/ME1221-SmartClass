from smartclass.smartclassroom.models import Question, Feedback
from smartclass.smartclassroom.serializers import VoteSerializer, FeedbackSerializer, VoteDetailSerializer
from smartclass.smartclassroom.permission import IsStudent, IsTeacher, IsTeacherOrReadOnly, IsStudentOrReadOnly
from smartclass.smartclassroom.throttle import CreateFeedbackThrottle
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User


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


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        groups = User.objects.get(username=user).groups.values_list('name', flat=True).distinct()
        groupList = [group for group in groups]
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'groups': groupList
        })
