from rest_framework import mixins, generics, permissions, status
from rest_framework.response import Response

from .serializers import MemberCreateSerializer

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
        
    