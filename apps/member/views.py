from rest_framework import mixins, generics, permissions, status
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MemberCreateSerializer, CustomTokenObtainSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    로그인

    ---
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomTokenObtainSerializer


class CreateMember(generics.GenericAPIView, mixins.CreateModelMixin):
    """ 
    회원 생성
    
    ---
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberCreateSerializer
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        print(args)
        print(kwargs)
        return Response(data="", status=status.HTTP_201_CREATED)
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        print(args)
        print(kwargs)
        return super().create(request, *args, **kwargs)
        
    