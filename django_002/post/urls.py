from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/',views.create,name='create'),
    path('<int:id>/detail/',views.detail, name='detail'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('model_create', views.model_create, name='model_create'),
    path('<int:id>/model_update', views.model_update, name='model_update')
    
]
