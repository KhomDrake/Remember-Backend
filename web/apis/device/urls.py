from django.urls import path, include
from .views import DeviceView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', DeviceView, basename='api.device')

urlpatterns = [
    path('', include(router.urls)),
]