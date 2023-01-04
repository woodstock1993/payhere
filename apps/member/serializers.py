import re, logging, jwt
from collections import OrderedDict

from django.contrib.auth import authenticate

from rest_framework import serializers, exceptions
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import (
    PasswordField,
    TokenObtainPairSerializer,     
    TokenRefreshSerializer)

from .models import Member
from apps.member import utils

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.EmailField()
        self.fields['password'] = PasswordField()
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)        
        token['name'] = user.name        
        return token
    
    def validate(self, attrs):
        logging.info("login validate")
        email = attrs[self.username_field]
        password = attrs['password']        
        
        try:
            Member.objects.get(email=email)
        except Member.DoesNotExist:
            raise exceptions.NotFound(f'해당 {email}이 존재하지 않습니다')

        user = authenticate(email=email, password=password)
        if user is None:
            raise exceptions.NotFound(f'패스워드가 일치하지 않습니다')

        data = super(CustomTokenObtainSerializer, self).validate(attrs) 
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        logging.info('refresh token')
        refresh = attrs['refresh']

        sign_key = api_settings.SIGNING_KEY
        algorithm = api_settings.ALGORITHM

        decode = jwt.decode(refresh, sign_key, algorithms=[algorithm])
        email = decode['email']

        member = Member.objects.get(email=email)


class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, validators=[utils.password_validator])
    email = serializers.EmailField()
    password = PasswordField()

    def validate_name(self, value):
        if len(value) <= 0:
            raise exceptions.ValidationError('이름 한글자 이상')        

    def validate_password(self, value):        
        if len(value) < 8:
            raise exceptions.ValidationError('비밀번호 최소 8자 이상')
        elif re.search('[0-9]+', value) is None:
            raise exceptions.ValidationError('최소 1개 이상의 숫자 포함')
        elif re.search('[a-zA-Z]+', value) is None:
            raise exceptions.ValidationError('최소 1개 이상의 영어 소문자 또는 대문자 포함')

    def validate(self, attrs):
        email = attrs.get('email')        
        queryset = Member.objects.filter(email=email)
        if queryset:
            raise exceptions.ValidationError("중복된 email입니다.")
        return super().validate(attrs)

    class Meta:
        model = Member
        fields= ['email', 'name', 'password']



class ResponseMemberSerializer(serializers.Serializer):
    def join(self, validated_data):
        logging.info('create user')

        email = validated_data.get('email')
        password = validated_data.get('password')
        name = validated_data.get('name')

        member =Member(
            email=email,
            name=name
        )
        member.set_password(password)
        member.save()
        return member

    def to_representation(self, instance):
        data = {
            'email': instance.email,
            'name': instance.name
        }
        return data


    class Meta:
        model = Member
        fields = ["email", "name"]
        swagger_schema_fields = {
            'description': "Member Created",
            'example': OrderedDict(
                [
                    ("email", "gildong@naver.com"),
                    ("name", "홍길동")
                ]
            )
        }        