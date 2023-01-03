from django.contrib import admin
from django.urls import path, include

from .views import CreateMember, CustomTokenObtainPairView

urlpatterns = [
    path('member/login/', CustomTokenObtainPairView.as_view()),
    path('member/', CreateMember.as_view()),
]