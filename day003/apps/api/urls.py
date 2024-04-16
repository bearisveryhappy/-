from django.urls import path,include,re_path
from apps.api import views
urlpatterns = [
    path('index/<str:role>/',views.anth),
    # re_path(r'login/(?P<a1>\d+)/(?P<a2>\w+)/', views.login,name='v2'),
    path('login/', views.login, name='v2'),
]