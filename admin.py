from django.contrib import admin
from gestionPedidos.models import Clientes
from gestionPedidos.models import Articulos
from gestionPedidos.models import Pedidos

admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)