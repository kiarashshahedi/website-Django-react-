from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer, ChangePasswordSerializer
from django.contrib.auth import get_user_model
from .permissions import IsSeller
from .serializers import CustomTokenObtainPairSerializer




User = get_user_model()

class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuyerProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # View buyer's profile information
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        # Update buyer profile information
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SellerProfileView(APIView):
    permission_classes = [IsAuthenticated, IsSeller]

    def get(self, request):
        # View seller's profile information
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        # Update seller profile information
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data['old_password']):
                return Response({"old_password": "Wrong password"}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.data['new_password'])
            user.save()
            return Response({"status": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SellerProductAdminView(APIView):
    permission_classes = [IsAuthenticated, IsSeller]

    def get(self, request):
        # Retrieve all products for the seller
        # Placeholder response (replace with actual product logic)
        return Response({"products": []})

    def post(self, request):
        # Add a new product for the seller
        # Placeholder response (replace with actual product creation logic)
        return Response({"message": "Product created"}, status=status.HTTP_201_CREATED)

    def put(self, request, product_id):
        # Update an existing product for the seller
        # Placeholder response (replace with actual product update logic)
        return Response({"message": f"Product {product_id} updated"}, status=status.HTTP_200_OK)

    def delete(self, request, product_id):
        # Delete a product for the seller
        # Placeholder response (replace with actual product deletion logic)
        return Response({"message": f"Product {product_id} deleted"}, status=status.HTTP_200_OK)



class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom JWT login view using TokenObtainPairSerializer for username and password authentication.
    """
    serializer_class = CustomTokenObtainPairSerializer