from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import  reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
##formularios ----------------------
from apps.administracion.forms import VesselForm, ServiceForm, TypeOfCargoForm, CustomerForm, ChangeUserToActivatedForm, StatusIdentForm
##modelos --------------------------
from apps.administracion.models import Customer, Service, TypeOfCargo, Vessel, StatusIdent
##generic view hiperclases ---------
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
##modelo de usuarios ---------------
from apps.users.models import CustomUser
# Create your views here.


def index(request):
  return render(request, 'administracion/index.html')

##Vista de inicio para administradores de bratton
class IndexView( LoginRequiredMixin, PermissionRequiredMixin ,TemplateView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    template_name = 'administracion/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['vessels'] = Vessel.objects.all()
        context['customers'] = Customer.objects.all()
        context['services'] = Service.objects.all()
        context['tocs'] = TypeOfCargo.objects.all()
        return context

class StatusIdentUpdate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = '/users/login/'
    redirect_field_name = '/administracion/'
    permission_required = 'users.validate_user'
    model = StatusIdent
    form_class = StatusIdentForm
    template_name = 'administracion/status/update.html'
    success_url = reverse_lazy('administracion:index')

#Views

##view de solicitudes para dar de alta usuarios
class SolicitudesList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = '/user/login/'
    permission_required = 'users.validate_user'
    model = CustomUser
    template_name = 'administracion/users/change_user.html'

    def get_queryset(request):
        return CustomUser.objects.filter(is_validated=False).filter(is_superuser=False).filter(is_staff=False)

##view para el cambio de estado de los usuarios
class ChangeUserToActivated(LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    login_url = '/users/login/'
    model = CustomUser
    permission_required = 'users.validate_user'
    form_class = ChangeUserToActivatedForm
    template_name = 'administracion/users/user_update_page.html'
    success_url = reverse_lazy('administracion:solicitudes')

##vista de cargas (Customers, Services y Type of cargo's )
class CargasView(LoginRequiredMixin, PermissionRequiredMixin ,TemplateView):
    login_url = '/users/login/'
    template_name = 'administracion/cargas-list.html'
    permission_required = 'users.validate_user'
    def get_context_data(self, **kwargs):
        context = super(CargasView, self).get_context_data(**kwargs)
        context['customers'] = Customer.objects.order_by('customer')
        context['services'] = Service.objects.order_by('service')
        context['tocs'] = TypeOfCargo.objects.order_by('type')
        return context  

##view para cargar vessels
class VesselCreate (LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    login_url = '/users/login/'
    redirect_field_name = '/administracion/'
    permission_required = 'users.validate_user'
    model = Vessel
    form_class = VesselForm
    template_name = 'administracion/vessel/update.html'
    success_url = reverse_lazy('administracion:index')

##view para actualizar vessels
class VesselUpdate (LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    login_url = '/users/login/'
    #redirect_field_name = 'redirect_to'
    model = Vessel
    permission_required = 'users.validate_user'
    form_class = VesselForm
    template_name = 'administracion/vessel/update.html'
    success_url = reverse_lazy('administracion:index')

##view para borrar vessels
class VesselDelete (LoginRequiredMixin, PermissionRequiredMixin ,DeleteView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = Vessel
    template_name = 'administracion/vessel/delete.html'
    success_url = reverse_lazy('administracion:index')

##Cargar services
class ServiceCreate (LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = Service
    form_class = ServiceForm
    template_name = 'administracion/service/update.html'
    success_url = reverse_lazy('administracion:cargas')

##Actualizar services
class ServiceUpdate (LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = Service
    form_class = ServiceForm
    template_name = 'administracion/service/update.html'
    success_url = reverse_lazy('administracion:cargas')

##Borrar services
class ServiceDelete (LoginRequiredMixin, PermissionRequiredMixin ,DeleteView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = Service
    template_name = 'administracion/service/delete.html'
    success_url = reverse_lazy('administracion:cargas')

##Cargar types of cargo (toc)
class TypeOfCargoCreate (LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = TypeOfCargo
    form_class = TypeOfCargoForm
    template_name = 'administracion/toc/update.html'
    success_url = reverse_lazy('administracion:cargas')

##Actualizar tocs
class TypeOfCargoUpdate (LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = TypeOfCargo
    form_class = TypeOfCargoForm
    template_name = 'administracion/toc/update.html'
    success_url = reverse_lazy('administracion:cargas')

##Borrar tocs
class TypeOfCargoDelete (LoginRequiredMixin, PermissionRequiredMixin ,DeleteView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = TypeOfCargo
    template_name = 'administracion/toc/delete.html'
    success_url = reverse_lazy('administracion:cargas')

##Cargar customer
class CustomerCreate (LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = Customer
    form_class = CustomerForm
    template_name = 'administracion/customer/update.html'
    success_url = reverse_lazy('administracion:cargas')

##Actualizar customer
class CustomerUpdate (LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = Customer
    form_class = CustomerForm
    template_name = 'administracion/customer/update.html'
    success_url = reverse_lazy('administracion:cargas')

##Borrar customer
class CustomerDelete (LoginRequiredMixin, PermissionRequiredMixin ,DeleteView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    redirect_field_name = '/administracion/'
    model = Customer
    template_name = 'administracion/customer/delete.html'
    success_url = reverse_lazy('administracion:cargas')

##--------------------
class IndexList (LoginRequiredMixin, PermissionRequiredMixin ,ListView):
    login_url = '/users/login/'
    permission_required = 'users.validate_user'
    model = Vessel
    template_name = 'administracion/index.html'
