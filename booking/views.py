from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum  # Importe o Sum do Django models
from .models import Reserva
from .forms import ReservaForm
from datetime import date, datetime, time, timedelta
from django.contrib import messages
from django.utils import timezone




def listar_conselho_de_classe(request):
    reservas = Reserva.objects.all()
    return render(request, "listar_conselho_de_classe.html", {"reservas": reservas})



def add_conselho_de_classe(request):
    return render(request, "booking/add_conselho_de_classe.html")

def lancar_conselho_declasse(request):
     return render(request, "booking/lancar_conselho_declasse.html")


def visualizar_conselho_de_classe(request):
    reservas = Reserva.objects.all()
    return render(request, "booking/visualizar_conselho_de_classe.html", {"reservas": reservas})



def criar_ata_conselho(request):
    return render(request, "booking/criar_ata_conselho.html")
