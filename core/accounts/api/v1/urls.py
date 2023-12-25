from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='api-register'),

    path('token/login/', views.CustomObtainAuthToken.as_view(), name='api-login-token'),
    path('token/logout/', views.CustomDeleteAuthTokenApiView.as_view(), name='api-logout-token'),

    path('jwt/create-token/', TokenObtainPairView.as_view(), name='jwt_obtain_pair'),
    path('jwt/refresh-token/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify-token/', TokenVerifyView.as_view(), name='jwt_verify'),
]
