from django.urls import path

from .import views

urlpatterns = [
    
    path('singup', views.registers,name='singup'),
    path('user/profile', views.profile,name='profile'),
    path('user/login', views.user_login,name='login'),
    path('user/logout', views.user_logout,name='logout'),
    path('user/change/profile', views.profile_change,name='profile_change'),
    path('buy/<int:id>/', views.buy_now,name='buy_now'),
]