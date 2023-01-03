from django.urls import path
from apps.member.views import CustomTokenObtainPairView

urlpatterns = [
    path('post/create', CustomTokenObtainPairView.as_view()),
]