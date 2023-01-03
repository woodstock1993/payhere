import logging

from django.db import transaction

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import MemberSerializer, JoinUserSerializer, CustomTokenObtainSerializer


class CreateUser(viewsets.ViewSet):
    """ 
    회원 가입
    
    ---
    """
    permission_classes = [permissions.AllowAny]
    user_response = openapi.Response("가입성공", JoinUserSerializer)

    @swagger_auto_schema(
        security=[],
        responses={status.HTTP_201_CREATED: user_response},
        request_body=JoinUserSerializer
    )
    @transaction.atomic
    def create_user(self, request):
        logging.info("create member user")
        serializer = JoinUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.join(request.data)
        serializer = MemberSerializer(serializer)

        print(f'serializer.data: {serializer.data}')

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    로그인

    ---
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainSerializer
        
    