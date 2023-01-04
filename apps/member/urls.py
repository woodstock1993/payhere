from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CreateUser, CustomTokenObtainPairView, LogOut

join_user = CreateUser.as_view({"post": "join_user_view"})

urlpatterns = [
    path('member/login', CustomTokenObtainPairView.as_view()),
    path('member/logout', LogOut.as_view()),
    path('member/join', join_user, name='join_user'),
    path('member/token/refresh', TokenRefreshView.as_view()),
]