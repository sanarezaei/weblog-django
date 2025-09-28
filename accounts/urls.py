from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm, ResetPasswordConfirmForm, ResetPasswordConfirmForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='authentication/login.html',
        form_class=UserLoginForm,
        redirect_authenticated_user=True
        ), name='login'),

    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html',
    form_class=ResetPasswordConfirmForm), 
    name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),

    path('', views.homepage, name='homepage'), 
    ]