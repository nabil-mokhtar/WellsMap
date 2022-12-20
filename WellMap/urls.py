from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from map.views import wellsViewSet

router = routers.DefaultRouter()
router.register(r'wells', wellsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]


