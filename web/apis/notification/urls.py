from django.urls import path, include
from .views import NotificationView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', NotificationView, basename='api.notification')

urlpatterns = [
    path('', include(router.urls))
]

