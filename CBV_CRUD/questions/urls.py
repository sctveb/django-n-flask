from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'questions'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('create/', views.create.as_view(), name='create'),
    path('<int:pk>/', views.read.as_view(), name='read'),
    path('update/<int:pk>', views.update.as_view(), name='update'),
    path('delete/<int:pk>', views.delete.as_view(), name='delete'),

]
