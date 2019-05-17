from django.conf.urls import url, include
from apps.users import views
from django.views.generic.base import TemplateView
#from apps.users.views import vessel_list
urlpatterns = [
    url(r'^home',TemplateView.as_view(template_name='index.html')),
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url(r'^tracking/', views.MyVesselListView.as_view(), name='home')
]
