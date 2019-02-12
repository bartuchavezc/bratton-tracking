from django.contrib import admin

from apps.administracion.models import Customer, Service, TypeOfCargo, Vessel, StatusIdent

# Register your models here.

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(TypeOfCargo)
admin.site.register(Vessel)
admin.site.register(StatusIdent)
