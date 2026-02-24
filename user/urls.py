from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('add/', views.SignUpView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/', views.UserUpdateView.as_view(), name='edit_user'),
    path('delete/', views.UserDeleteView.as_view(), name='delete_user'),
    path('profile/<int:pk>/', views.ViewProfile.as_view(), name='view_profile'),
]
