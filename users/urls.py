from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView 


urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register_user'),
    path('profile/', views.UserProfile.as_view(), name='user_profile'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
]
