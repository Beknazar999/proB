from django.urls import path
from .views import ChangePasswordView, LoginView, RegisterView, TokenRefreshView, TokenVerifyView, GetUserView

urlpatterns = [
    path('api/v1/auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/v1/auth/login/', LoginView.as_view(), name='login'),
    path('api/v1/auth/register/', RegisterView.as_view(), name='register'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/v1/auth/token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('api/v1/auth/user/', GetUserView.as_view(), name='get-user'),
]