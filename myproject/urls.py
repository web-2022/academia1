"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings  # Importa settings correctamente
from django.conf.urls.static import static  # Importa para servir archivos media
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación
from courses import views as course_views  # Para registrar la vista de register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),    
    path('register/', course_views.register, name='register'),  # URL para registro
    
# URLs de autenticación (usando las vistas genéricas de Django)
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL para la vista de login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL para la vista de logout
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)