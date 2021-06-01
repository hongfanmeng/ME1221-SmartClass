from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from utils.views import AuthToken

urlpatterns = [
    path('api-token-auth/', AuthToken.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
