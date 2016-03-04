from django.conf.urls import patterns, url
from brand_profiles import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^api/$', views.api_view, name='index'),
        url(r'^work/$', views.work_view, name='work'),
        url(r'^education/$', views.education_view, name='education'),
        url(r'^contact/$', views.contact_view, name='contact'),
        url(r'^api/analyse/$', views.sample, name='analyse'),
     
    )
		