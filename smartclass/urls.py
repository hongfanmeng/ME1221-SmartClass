from django.urls import path
from smartclass.smartclassroom import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.apps import apps

app_models = apps.get_app_config('smartclass').get_models()

for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.AuthToken.as_view()),
    path('votes/', views.VoteList.as_view()),
    path('votes/<int:pk>/', views.VoteDetail.as_view()),
    path('feedbacks/', views.FeedbackList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
