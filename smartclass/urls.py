from django.urls import include, path
from smartclass.smartclassroom import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('votes/', views.VoteList.as_view()),
    path('votes/<int:pk>/', views.VoteDetail.as_view()),
    path('feedbacks/', views.FeedbackList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
