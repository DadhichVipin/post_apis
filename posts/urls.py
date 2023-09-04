from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api/login/', obtain_auth_token, name='user-login'),
]
