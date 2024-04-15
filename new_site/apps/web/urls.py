from django.urls import path, include
from apps.web import  views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login,name='login')
]
