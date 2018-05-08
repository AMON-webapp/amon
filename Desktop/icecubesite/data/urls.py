from django.conf.urls import url 
from . import views 

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    ##url(r'^observe/', views.observe, name='observatories'),
    ##url(r'^about/', views.about, name="about"),
    url(r'^data/', views.data, name="data"), 
    url(r'^admin/', admin.site.urls),
]

