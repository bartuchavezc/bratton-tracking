from django.db import models

##Customer (cliente de bratton)
class Customer (models.Model):
    customer = models.CharField(max_length=100)
    referente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=150)
    def __str__(self):
        return '{}'.format(self.customer)

##tipo de servicio que presta
class Service (models.Model):
    service = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.service)

##tipo de carga del envio
class TypeOfCargo (models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.type)

##identificador de estatus de la carga (no iniciado, iniciado, en curso)
class StatusIdent(models.Model):
    name = models.CharField(editable=True, max_length=100)
    def __str__(self):
        return '{}'.format(self.name)

##Carga, Container ,etc.        
class Vessel (models.Model):
    #identificador unico del vessel
    bl_number = models.CharField(editable=True, max_length=100)
    ##claves foraneas
    customer = models.ForeignKey(Customer, null=True, blank=True , on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True , on_delete=models.CASCADE)
    type_of_cargo = models.ForeignKey(TypeOfCargo, null=True, blank=True , on_delete=models.CASCADE)
    #puertos
    pol = models.CharField(max_length=100)
    pod = models.CharField(max_length=100)
    #fechas
    etd = models.DateField()
    eta = models.DateField()
    #identificadores que cargan desde administracion
    contenedor = models.TextField(max_length=140)
    ref = models.TextField(max_length=140)
    status = models.TextField(max_length=140)
    #indentificador de estatus
    status_ident = models.ForeignKey(StatusIdent, null=True, blank=True, on_delete=models.CASCADE)
