"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_intro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('lunch/', views.lunch),
    path('lotto/', views.lotto),
    path('hello/<str:name>/', views.hello),
    path('cube/<int:number>', views.cube),
    path('todos/', include('todo.urls'))
]

# 인자 컨버터
# str : 스트링
# int : 0 또는 양의 정수
# slug : 문자 또는 숫자 하이픈 밑줄 
#         show-me-the-money