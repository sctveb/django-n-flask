from django.contrib import admin
from django.urls import path, include
from . import views
app_name='account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),


]