from django.urls import path,include,re_path
from apps.api import views
urlpatterns = [
    path('index/',views.anth,name='anth'),
    path('login/', views.login,name='login'),
]