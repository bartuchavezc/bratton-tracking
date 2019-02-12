from django.db import models

# Create your models here.
class Customer (models.Model):
    customer = models.CharField(max_length=100)
    referente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=150)
    def __str__(self):
        return '{}'.format(self.customer)

class Service (models.Model):
    service = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.service)

class TypeOfCargo (models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.type)

class StatusIdent(models.Model):
    name = models.CharField(editable=True, max_length=100)
    def __str__(self):
        return '{}'.format(self.name)
        
class Vessel (models.Model):
    bl_number = models.CharField(editable=True, max_length=100)
    customer = models.ForeignKey(Customer, null=True, blank=True , on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True , on_delete=models.CASCADE)
    type_of_cargo = models.ForeignKey(TypeOfCargo, null=True, blank=True , on_delete=models.CASCADE)
    pol = models.CharField(max_length=100)
    pod = models.CharField(max_length=100)
    etd = models.DateField()
    eta = models.DateField()
    contenedor = models.TextField(max_length=140)
    ref = models.TextField(max_length=140)
    status = models.TextField(max_length=140)
    status_ident = models.ForeignKey(StatusIdent, null=True, blank=True, on_delete=models.CASCADE)
