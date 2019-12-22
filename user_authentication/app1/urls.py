from django.urls import path
from . import views


app_name = 'app1'

urlpatterns = [
    path('registration/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('special/',views.special, name = 'special'),
    path('logout/', views.user_logout, name = 'logout')
]