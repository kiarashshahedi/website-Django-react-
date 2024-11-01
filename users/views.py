from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import MyUser

# Register 
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login 
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data['mobile']
            password = serializer.validated_data['password']
            user = authenticate(request, mobile=mobile, password=password)
            if user:
                login(request, user)
                return Response(UserSerializer(user).data)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

# Buyer Dashboard 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buyer_dashboard_view(request):
    if request.user.is_seller:
        return Response({"error": "Access denied"}, status=403)
    # Sample response with buyer-specific data
    return Response({
        "message": "Welcome to the Buyer Dashboard",
        "data": "Buyer-specific data here"
    })

# Seller Dashboard 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def seller_dashboard_view(request):
    if not request.user.is_seller:
        return Response({"error": "Access denied"}, status=403)
    # Sample response with seller-specific data
    return Response({
        "message": "Welcome to the Seller Dashboard",
        "data": {
            "products": [],  # Seller's products data
            "orders": [],    # Seller's orders data
            # Additional seller-specific info
        }
    })