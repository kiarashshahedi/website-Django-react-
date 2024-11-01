from django.urls import path
from .views import RegisterView, LoginView, LogoutView, buyer_dashboard_view, seller_dashboard_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/buyer/', buyer_dashboard_view, name='buyer_dashboard'),
    path('dashboard/seller/', seller_dashboard_view, name='seller_dashboard'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
