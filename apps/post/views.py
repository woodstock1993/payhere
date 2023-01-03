from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from .models import Post
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """
    CRUD
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]