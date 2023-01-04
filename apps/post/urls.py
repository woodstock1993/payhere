from django.urls import path
from . import views


urlpatterns = [
    path(
        'post/<int:id>', 
        views.PostGetUpdateDestory.as_view(),
        name='post-get'
    ),
    path(
        'post', 
        views.PostListCreate.as_view(),
        name='post-create-destory'
    ),
    path(
        'post/<int:id>/copy',
        views.PostCopy.as_view(),
        name='post-copy'
    ),
]