import re, logging
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.serializers import (
    PasswordField,
    TokenObtainPairSerializer, 
    TokenObtainSerializer, 
    TokenRefreshSerializer)

from .models import Member
from apps.member import utils

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.EmailField()
        self.fields['password'] = PasswordField()
    
    def validate(self, attrs):
        logging.info("login validate")
        email = attrs[self.username_field]        
        try:
            Member.objects.get(email=email)
        except Member.DoesNotExist:
            raise exceptions.NotFound(f'해당 {email}이 존재하지 않습니다')

class MemberSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField(write_only=True, validators=[utils.password_validator])

    def validate_name(self, value):
        if len(value) <= 0:
            raise exceptions.ValidationError('이름 한글자 이상')        

    def validate_password(self, value):        
        if len(value) < 8:
            raise exceptions.ValidationError('비밀번호 최소 8자 이상')
        elif re.search('[0-9]+', value) is None:
            raise exceptions.ValidationError('최소 1개 이상의 숫자 포함')
        elif re.search('[a-zA-Z]+', value) is None:
            raise exceptions.ValidationError('최소 1개 이상의 숫자 포함')

    def validate(self, attrs):
        email = attrs.get('email')        
        queryset = Member.objects.filter(email=email)
        if queryset:
            raise exceptions.ValidationError("중복된 email입니다.")
        return super().validate(attrs)
    
    def create(self, validated_data):
        print(f'validated_data:{validated_data}')
        member = Member.objects.create(**validated_data)
        return member

    class Meta:
        model = Member
        fields = ['email', 'name', 'password']        
        

class JoinUserSerializer(serializers.Serializer):
    user = MemberSerializer()

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