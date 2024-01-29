from django.urls import path
from users.views import RegisterNewUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)

urlpatterns = [
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", RegisterNewUser.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
