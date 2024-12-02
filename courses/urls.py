# courses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.course_list, name='course_list'),
    path('ciclos/', views.ciclos, name='ciclos'),
    path('contactanos/', views.contactanos, name='contactanos'), 
    path('<slug:course_slug>/capitulo/<slug:chapter_slug>/', views.capitulo, name='capitulo'),
    path('<slug:slug>/', views.course_detail, name='course_detail'),

]