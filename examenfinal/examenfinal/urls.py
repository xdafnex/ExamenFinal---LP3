"""
URL configuration for examenfinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name = "index"),
    path('personas/', views.personas, name = "personas"),
    path('agregar_persona/', views.agregar_persona, name='agregar_persona'),
    path('eliminar_persona/<int:id>/', views.eliminar_persona, name="eliminar_persona"),
    path('editar_persona/<int:id>/', views.editar_persona, name='editar_persona'),
]
