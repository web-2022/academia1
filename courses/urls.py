# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.course_list, name='course_list'),
    path('ciclos/', views.ciclos, name='ciclos'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    
]
