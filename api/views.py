from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Group, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """A viewset for processing requests for getting posts
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """A viewset for processing requests for getting comments
    """
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """A viewset for processing requests for getting groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    http_method_names = ('post', 'get',)


class FollowViewSet(viewsets.ModelViewSet):
    """A viewset for processing requests for getting followings
    """
    serializer_class = FollowSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOrReadOnly,
    ]
    http_method_names = ('post', 'get',)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username',)

    def get_queryset(self):
        return self.request.user.following

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
