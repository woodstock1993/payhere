import logging

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework import serializers

from .utils import password_validator
from .models import Post

from rest_framework_simplejwt.serializers import (
    PasswordField,
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
    TokenObtainSerializer
)


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


class PostSerializer(serializers.ModelSerializer):
    def validate_balance(self, attrs):
        balance = attrs.get('balance')
        if balance < 0:
            raise exceptions.ValidationError("Field balance must be zero or positive")

    class Meta:
        model = Post
        fields = '__all__'


class GenericPostSerializer(serializers.Serializer):
    author = serializers.CharField()
    body = serializers.CharField()
    balance = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def validate(self, attrs):
        author = attrs['author']
        if len(author) == 0:
            raise exceptions.ValidationError('적어도 한글자 이상이어야 합니다')
        return super().validate(attrs)


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'body', 'balance']
        read_only_fields = ['author']

    def create(self, validated_data):        
        instance = Post.objects.create(**validated_data)
        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)        
        data['author'] = self.context['request'].user.__str__()
        return data


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'balance']

    def update(self, validated_data):        
        id = validated_data['id']
        body = validated_data['body']
        balance = validated_data['balance']        
        
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise exceptions.NotFound(f'해당 가계부가 없습니다.')
        
        post.body = body
        post.balance = balance
        post.save()        
        return post


class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'body', 'balance']


