from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    #filter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ('exact', 'icontains'),
        'body': ['icontains'],
        'author__username': ['exact'],
    }
    
    def perform_create(self, serializer):
        # Set the author of the post to the current authenticated user
        serializer.save(author=self.request.user)
