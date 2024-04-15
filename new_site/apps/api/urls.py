
from django.urls import path, include,re_path
from apps.api import  views
urlpatterns = [
    path('index/', views.index),
    path('news/<path:nid>/edit/', views.index),
    re_path('login/(\d+)/(\w+)', views.login,name='v2')
]
