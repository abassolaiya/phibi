from django.urls import path, include
from django.contrib.auth import views as auth_views
 # django.contrib.auth.logout()
from . import views


urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='account_login'),
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('sub_register/', views.register, name='account_signup'),
    path('edit/', views.edit, name='edit'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # # path('logout', LogoutView.as_view(), name='logout'),
    # path('', views.dashboard, name='dashboard'),
    # path('', include('django.contrib.auth.urls')),
    # path('register/', views.register, name='register'),
    # path('edit/', views.edit, name='edit'),
]
