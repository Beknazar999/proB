
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer

class ChangePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
       
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class TokenRefreshView(APIView):
    def post(self, request, *args, **kwargs):
        
        return Response({'message': 'Token refreshed successfully'}, status=status.HTTP_200_OK)

class TokenVerifyView(APIView):
    def post(self, request, *args, **kwargs):
        
        return Response({'message': 'Token verified successfully'}, status=status.HTTP_200_OK)

class GetUserView(APIView):
    def get(self, request, *args, **kwargs):
       
        user_data = {'username': request.user.username, 'email': request.user.email}
        return Response(user_data, status=status.HTTP_200_OK)
