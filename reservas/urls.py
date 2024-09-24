from django.contrib import admin
from django.urls import path
from booking.views import listar_conselho_de_classe, add_conselho_de_classe, lancar_conselho_declasse, visualizar_conselho_de_classe, criar_ata_conselho

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_conselho_de_classe, name='listar_conselho_de_classe'),
    path('reservas/add_conselho_de_classe/', add_conselho_de_classe, name='add_conselho_de_classe'),
    path('reservas/lancar_conselho_declasse/', lancar_conselho_declasse, name='lancar_conselho_declasse'),
    path('reservas/visualizar_conselho_de_classe/', visualizar_conselho_de_classe, name='visualizar_conselho_de_classe'),
    path('reservas/criar_ata_conselho/', criar_ata_conselho, name='criar_ata_conselho'),
]
