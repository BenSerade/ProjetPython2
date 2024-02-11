"""
URL configuration for ProjetPython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from ProjetPython import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/create/', views.create_session, name='create_session'),
    path('sessions/<int:pk>/', views.session_detail, name='session_detail'),
    path('sessions/<int:session_pk>/submit/', views.submit_form, name='submit_form'),
    # Mettre à jour le chemin pour faire référence à une vue de connexion existante
    path('login/', views.login_view, name='login'),
    path('formulaire/', views.formulaire_client, name='formulaire_client'),
]