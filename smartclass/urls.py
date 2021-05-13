from django.urls import include, path
from smartclass.smartclassroom import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('votes/', views.VoteList.as_view()),
    path('votes/<int:pk>/', views.VoteDetail.as_view()),
    path('feedbacks/', views.FeedbackList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
