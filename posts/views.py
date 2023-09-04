from django.shortcuts import render
from rest_framework import viewsets
from posts.permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    #filter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'title': ['exact', 'icontains'],
        'body': ['exact','icontains'],
        'author__username': ['exact'],
    }

    # pagination
    pagination_class = PageNumberPagination

    # Rate Limiting
    throttle_classes = [UserRateThrottle]

    def perform_create(self, serializer):
        # Set the author of the post to the current authenticated user
        serializer.save(author=self.request.user)
