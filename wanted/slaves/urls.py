from django.conf.urls import url

from . import views , forms


app_name='slaves'
urlpatterns = [
    url(r'^$', views.ShowSl),
    url(r'^a$', views.ListSlavesView.as_view(), name='list'),
    url(r'^add$', views.CreateSlave.as_view(),name="add" ),
    url(r'^sla(?P<pk>\d+)$',  views.DetailSlaveView.as_view(), name='detail'),
    #url(r'^a(?P<pk>\d+)$',  views.DetailSlaveView.as_view(), name='detail'),

    # url(r'^sl', 'slaves.urls') ,
    # url(r'^admin/', admin.site.urls),
]
