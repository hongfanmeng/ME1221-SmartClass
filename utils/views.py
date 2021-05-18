from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User


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
