from rest_framework import serializers
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer, TokenObtainSerializer, TokenRefreshSerializer)


from .models import Member

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    pass

class MemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['email', 'password']


class PwCheckSerializer(serializers.Serializer):
    password = serializers.CharField(validators=[])
        