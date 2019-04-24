from django.conf.urls import url, include
from apps.administracion.views import index, IndexList, IndexView, CargasView, \
    VesselCreate, VesselUpdate, VesselDelete, \
    ServiceCreate, ServiceUpdate, ServiceDelete, \
    TypeOfCargoCreate, TypeOfCargoUpdate, TypeOfCargoDelete, \
    CustomerCreate, CustomerUpdate, CustomerDelete, SolicitudesList, ChangeUserToActivated, StatusIdentUpdate
from django.contrib.auth.decorators import login_required
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^solicitudes', SolicitudesList.as_view(), name='solicitudes'),
    url(r'^change_user/(?P<pk>\d)/$', ChangeUserToActivated.as_view(), name='change_solicitud' ),
    url(r'^cargas/', CargasView.as_view(), name='cargas' ),
    url(r'^status/new', StatusIdentUpdate.as_view(), name='new_status'),
    ##clientes
    url(r'^vessel/new$', VesselCreate.as_view() , name="vessels_nuevo" ),
    url(r'^vessel/edit/(?P<pk>\d)/$', VesselUpdate.as_view() , name="vessels_update"),
    url(r'^vessel/delete/(?P<pk>\d)/$', VesselDelete.as_view() , name="vessels_delete"),
    ##customers
    url(r'^customers/new$', CustomerCreate.as_view() , name="customers_nuevo" ),
    url(r'^customer/list$', CustomerList.as_view() , name="customer_list" ),
    url(r'^customers/edit/(?P<pk>\d)/$', CustomerUpdate.as_view() , name="customers_update"),
    url(r'^customers/delete/(?P<pk>\d)/$', CustomerDelete.as_view() , name="customers_delete"),
    ##services
    url(r'^services/new$', ServiceCreate.as_view() , name="services_nuevo" ),
    url(r'^service/list$', ServiceList.as_view() , name="service_list" ),
    url(r'^services/edit/(?P<pk>\d)/$', ServiceUpdate.as_view() , name="services_update"),
    url(r'^services/delete/(?P<pk>\d)/$', ServiceDelete.as_view() , name="services_delete"),
    ##type of cargo
    url(r'^toc/new$', TypeOfCargoCreate.as_view() , name="tocs_nuevo" ),
    url(r'^toc/list$', TypeOfCargoList.as_view() , name="tocs_list" ),
    url(r'^toc/edit/(?P<pk>\d)/$', TypeOfCargoUpdate.as_view() , name="tocs_update"),
    url(r'^toc/delete/(?P<pk>\d)/$', TypeOfCargoDelete.as_view() , name="tocs_delete"),
]
