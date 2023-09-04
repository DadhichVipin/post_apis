from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework import permissions

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def perform_create(self, serializer):
        # Set the author of the post to the current authenticated user
        serializer.save(author=self.request.user)
