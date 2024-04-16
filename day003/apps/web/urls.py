from django.urls import path,include
from apps.web import views
urlpatterns = [
    path('news/',views.info),
    path('home/<int:nid>/', views.home),
]