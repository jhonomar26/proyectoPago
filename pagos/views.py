from django.shortcuts import render

# En views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import *
from .forms import *
from rest_framework import viewsets
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)
from .forms import IngresoForm
from django.http import JsonResponse
from .models import Ingreso
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                if request.POST["password1"] == request.POST["password2"]:
                    # Registro en la tabla de Usuarios de Django
                    if User.objects.filter(
                        username=form.cleaned_data["username"]
                    ).exists():
                        return render(
                            request,
                            "signup.html",
                            {
                                "form": form,
                                "error": "El nombre de usuario ya está en uso.",
                            },
                        )
                    user = User.objects.create_user(
                        username=form.cleaned_data["username"],
                        password=form.cleaned_data["password1"],
                    )
                    usuario = Usuario(
                        nomUsuario=form.cleaned_data["username"],
                        totalIngresos=0,
                        totalEgreso=0,
                        totalGanancias=0.0,
                        correoElectronico=form.cleaned_data["email"],
                    )
                    usuario.save()

                    # Autenticar y redirigir al usuario
                    login(request, user)
                    return redirect("home")
                else:
                    return render(
                        request,
                        "signup.html",
                        {
                            "form": form,
                            "error": "La contraseñas no coinciden",
                        },
                    )

            except IntegrityError as e:
                # Manejar la excepción de IntegrityError específica
                return render(
                    request,
                    "signup.html",
                    {"form": form, "error": "El usuario ya existe."},
                )
    else:
        form = RegistroForm()
    return render(request, "signup.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "POST":
        form = CustomInicioSesionForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                # user = Usuario.objects.get(username=username, password=password)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("home")
            except Usuario.DoesNotExist:
                return render(
                    request,
                    "signin.html",
                    {
                        "form": form,
                        "error": "La contraseña o el usuario son incorrectos",
                    },
                )
    else:
        form = CustomInicioSesionForm()
    return render(request, "signin.html", {"form": form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Ingreso
from .forms import IngresoForm


def ingresos(request):
    usuario = request.user
    usuario_obj = get_object_or_404(Usuario, nomUsuario=usuario.username)
    # Obtener todos los ingresos del usuario actualmente autenticado
    ingresos = Ingreso.objects.filter(Usuario_idUsuario=usuario_obj.idUsuario)

    # Calcular el total de ingresos
    total_ingresos = ingresos.aggregate(total=models.Sum("monto"))["total"] or 0

    # Renderizar la plantilla y pasar los ingresos y el total de ingresos a la plantilla
    return render(
        request,
        "ingresos.html",
        {"ingresos": ingresos, "total_ingresos": total_ingresos},
    )


def agregar_ingreso(request):
    usuario = request.user
    usuario_obj = get_object_or_404(Usuario, nomUsuario=usuario.username)

    if request.method == "POST":
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.Usuario_idUsuario = usuario_obj
            ingreso.save()
            return redirect("ingresos")

    else:
        form = IngresoForm()
    return render(request, "agregar_ingreso.html", {"form": form})


def eliminar_ingreso(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, pk=ingreso_id)
    if ingreso.Usuario_idUsuario == request.user:
        ingreso.delete()
        return redirect("ingresos")
    else:
        return redirect("home")


def actualizar_ingreso(request, ingreso_id):
    ingreso = get_object_or_404(Ingreso, pk=ingreso_id)
    if request.method == "POST":
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect("ingresos")
    else:
        form = IngresoForm(instance=ingreso)
    return render(request, "actualizar_ingreso.html", {"form": form})
