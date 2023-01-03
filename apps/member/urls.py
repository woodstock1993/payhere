from django.urls import path

from .views import CreateUser, CustomTokenObtainPairView

create_user = CreateUser.as_view({"post": "create_user"})

urlpatterns = [
    path('member/login/', CustomTokenObtainPairView.as_view()),
    path('member/join/user/', create_user, name='create_user'),
]