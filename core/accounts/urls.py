from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login-page'),
    path('register/', views.RegisterPageView.as_view(), name='register-page'),
    path('logout/', views.LogoutPageView.as_view(), name='logout-page'),
    path('api/v1/', include('accounts.api.v1.urls')),
]
