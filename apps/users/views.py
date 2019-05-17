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