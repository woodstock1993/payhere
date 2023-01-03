from django.urls import path

from .views import CreateUser, CustomTokenObtainPairView

join_user = CreateUser.as_view({"post": "join_user_view"})

urlpatterns = [
    path('member/login', CustomTokenObtainPairView.as_view()),
    path('member/join', join_user, name='join_user'),
]