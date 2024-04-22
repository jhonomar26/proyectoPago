"""
URL configuration for ProyectoPago project.

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
from pagos import views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("signin/", views.signin, name="signin"),
    path("ingresos/", views.ingresos, name="ingresos"),
    path('ingresos/agregar/', views.agregar_ingreso, name='agregar_ingreso'),
    path('ingresos/<int:ingreso_id>/actualizar/', views.actualizar_ingreso, name='actualizar_ingreso'),
    path('ingresos/<int:ingreso_id>/eliminar/', views.eliminar_ingreso, name='eliminar_ingreso'),
    # armar
    # path("pc/", views.ComponentsListView.as_view(), name="pc-list"),
    # path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    # path('armar-pc/', views.armar_pc, name='armar-pc'),
    # path('pc/<int:pk>/', views.PCDetailView.as_view(), name='detalle-pc'),
    # path('armar-pc/', views.ArmarPCView.as_view(), name='armar-pc'),
]
