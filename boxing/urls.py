from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from boxing.api import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'containers', views.ContainerViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'lendings', views.LendingViewSet)
router.register(r'media', views.MediaViewSet)
router.register(r'photos', views.PhotoViewSet)
router.register(r'related', views.RelatedViewSet)

# https://docs.djangoproject.com/en/1.8/howto/static-files/#serving-files-uploaded-by-a-user-during-development
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
