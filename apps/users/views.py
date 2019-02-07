from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from apps.users.forms import CustomUserCreationForm
from apps.users.models import CustomUser
from django.http import HttpResponseRedirect
from django.core import serializers
from apps.administracion.models import Vessel
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class MyVesselListView(LoginRequiredMixin, generic.ListView):

    login_url = '/users/login/'

    model = Vessel

    template_name = 'home.html'

    paginate_by = 10

    def get_queryset(self):
        return Vessel.objects.filter(customer = self.request.user.customer).order_by('bl_number')

''' def get_context_data(self, **kwargs):
    context = super(My, self).get_context_data(**kwargs)
    context['vessels_in_progress'] = Vessel.objects.filter(customer = self.user.customer).filter(stat = 2)
    context['vessels_finished'] = Service.objects.filter(customer = self.user.customer).filter(stat = 3)
    context['vessels_proximos'] = TypeOfCargo.filter(customer = self.user.customer).filter(stat = 1)
    return context '''
