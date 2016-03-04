from rest_framework import routers

from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import routers
from brand_profiles import views

router = routers.DefaultRouter()
router.register(r'brands', views.Brand_IdentitiesViewSet)
router.register(r'reviews', views.ReviewsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^djangoapi/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('brand_profiles.urls', namespace="brand_profiles")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)