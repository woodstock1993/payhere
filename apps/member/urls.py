from django.contrib import admin
from django.urls import path, include

from .views import CreateMember

urlpatterns = [
    path('member/', CreateMember.as_view()),
]