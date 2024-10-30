from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterUser, CustomTokenObtainPairView, BuyerProfileView, SellerProfileView,
    ChangePasswordView, SellerProductAdminView,
)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('buyer/profile/', BuyerProfileView.as_view(), name='buyer_profile'),
    path('seller/profile/', SellerProfileView.as_view(), name='seller_profile'),
    path('seller/admin/products/', SellerProductAdminView.as_view(), name='seller_admin'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

]
