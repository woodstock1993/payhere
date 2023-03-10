import logging

from django.db import transaction

from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import MemberSerializer, CustomTokenObtainSerializer, ResponseMemberSerializer


class CreateUser(viewsets.ViewSet):
    """ 
    회원 가입
    
    ---
    """
    permission_classes = (permissions.AllowAny,)

    response_dict = {
        status.HTTP_201_CREATED: None,
        f"{status.HTTP_201_CREATED}(MEMBER CREATED)": ResponseMemberSerializer,        
    }
    @swagger_auto_schema(
        security=[],
        responses=response_dict,
        request_body=MemberSerializer,
        )
    @transaction.atomic
    def join_user_view(self, request):
        logging.info("create member user")
        serializer = MemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = ResponseMemberSerializer()
        member = instance.join(request.data)
        serializer = ResponseMemberSerializer(member)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    로그인

    ---
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainSerializer


class LogOut(APIView):
    """
    로그아웃

    ---
    """ 
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access_token')
        return response