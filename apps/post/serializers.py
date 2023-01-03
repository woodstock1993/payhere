import logging

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework import serializers, ModelSerializer

from rest_framework_simplejwt.serializers import (
    PasswordField,
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
    TokenObtainSerializer
)

from .models import Ledger
from apps.member.models import Member


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.EmailField()
        self.fields["password"] = PasswordField()
    
    def validate(self, attrs):
        logging.info('login validate')
        email = attrs[self.username_field]

        try:
            Member.objects.get()
        except:
            pass
    


class PostSerializer(ModelSerializer):
    def validate_balance(self, attrs):
        balance = attrs.get('balance')
        if balance < 0:
            raise exceptions.ValidationError("Field balance must be zero or positive")

    class Meta:
        model = Ledger
        fields = '__all__'