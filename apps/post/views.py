from django.db import transaction

from rest_framework import permissions, status, exceptions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet, generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post
from .serializers import PostSerializer, GenericPostSerializer, CreatePostSerializer, UpdatePostSerializer, DeletePostSerializer

from drf_yasg.utils import swagger_auto_schema


class PostGetUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    """
    가계부

    ---
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GenericPostSerializer
        if self.request.method == 'PUT':
            return UpdatePostSerializer
        if self.request.method == 'DELETE':
            return DeletePostSerializer

    @swagger_auto_schema(
        operation_summary="가계부 조회",        
    )
    def retrieve(self, request, id):        
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)            
        except Post.DoesNotExist:
            raise exceptions.NotFound(f'해당 가계부가 없습니다.')
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        
    @swagger_auto_schema(
        operation_summary="가계부 업데이트",
        request_body=UpdatePostSerializer
    )
    def update(self, request, id, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        model_serializer = UpdatePostSerializer()

        dic = self.request.data
        dic.update({'id': id})
        obj = model_serializer.update(dic)
        return Response(data=PostSerializer(obj).data, status=status.HTTP_200_OK)

    @transaction.atomic
    @swagger_auto_schema(        
        operation_summary="가계부 삭제",
        responses={status.HTTP_200_OK: DeletePostSerializer}        
    )
    def destroy(self, request, id, *args, **kwargs):
        try:
            obj = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise exceptions.NotFound('가계부를 찾을 수 없습니다.')            
        serializer = DeletePostSerializer(obj)        
        obj.delete()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class PostListCreate(generics.ListCreateAPIView):
    """
    가계부

    ---
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]    
    serializer_class = CreatePostSerializer

    @transaction.atomic
    @swagger_auto_schema(        
        operation_summary="가계부 생성",
        responses={status.HTTP_201_CREATED: CreatePostSerializer}        
    )
    def create(self, request):        
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)        
        obj = Post(author=self.request.user, body=request.data['body'], balance=request.data['balance'])
        obj.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(        
        operation_summary="가계부 전체 조회",
        responses={status.HTTP_200_OK: DeletePostSerializer}        
    )    
    def list(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)