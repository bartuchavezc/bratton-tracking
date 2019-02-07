from django.conf.urls import url, include
from apps.users import views
#from apps.users.views import vessel_list
urlpatterns = [
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url(r'^tracking/', views.MyVesselListView.as_view(), name='home'),
    #url(r'^home/', vessel_list, name=vessel_list)
]
