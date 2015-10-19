from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from boxing.api import views
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'containers', views.ContainerViewSet)
router.register(r'items', views.ItemViewSet)

# https://docs.djangoproject.com/en/1.8/howto/static-files/#serving-files-uploaded-by-a-user-during-development
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


