from django import forms

from apps.administracion.models import Vessel, TypeOfCargo, Service, Customer, StatusIdent
from apps.users.models import CustomUser

class StatusIdentForm(forms.ModelForm):

    class Meta:
        model = StatusIdent

        fields = [
            'name',
        ]

        labels = {
            'name': 'Status Name',
        }

        widgets = {
            'name': forms.TextInput({'class': 'form-control'})
        }

class CustomerForm(forms.ModelForm):
#form clientes
    class Meta:
        model = Customer

        fields = [
            'customer',
        ]

        labels = {
            'customer': 'Customer',
        }

        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ChangeUserToActivatedForm(forms.ModelForm):

    class Meta:
        model = CustomUser

        fields = [
            'is_validated',
        ]

        labels = {
            'is_validated': 'Dar de alta',
        }

        widgets = {
            'is_validated': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'})
        }



#form tipos
class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service

        fields = [
            'service',
        ]

        labels = {
            'service': 'service',
        }

        widgets = {
            'service': forms.TextInput(attrs={'class': 'form-control'}),
        }


#form servicios
class TypeOfCargoForm(forms.ModelForm):

    class Meta:
        model = TypeOfCargo

        fields = [
            'type',
        ]

        labels = {
            'type': 'Type of cargo',
        }

        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
        }

#form servicios
class VesselForm(forms.ModelForm):

    class Meta:
        model = Vessel

        fields = [
            'bl_number',
            'customer',
            'service',
            'type_of_cargo',
            'pol',
            'pod',
            'etd',
            'eta',
            'contenedor',
            'ref',
            'status',
            'status_ident',
        ]

        labels = {
            'bl_number': 'BL Number',
            'customer': 'Customer',
            'service': 'Service',
            'type_of_cargo': 'Type of cargo',
            'pol': 'P.O.L',
            'pod': 'P.O.D',
            'etd': 'E.T.D',
            'eta': 'E.T.A',
            'contenedor': 'Contenedor',
            'ref': 'Referente',
            'status': 'Status',
            'status_ident': 'Satus Ident'
        }

        widgets = {
            'bl_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BL Number'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'type_of_cargo': forms.Select(attrs={'class': 'form-control'}),
            'pol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'P.O.L'}),
            'pod': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'P.O.D'}),
            'etd': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AAAA-MM-DD'}),
            'eta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'AAAA-MM-DD'}),
            'contenedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contenedor'}),
            'ref': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Referente'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Status'}),
            'status_ident': forms.Select(attrs={'class': 'form-control'}),
            }
