# myportfolio/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Updated URL pattern.
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Updated URL pattern.
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Optional: Password reset.
    path('', include('portfolio.urls')),  # App URLs.
]
