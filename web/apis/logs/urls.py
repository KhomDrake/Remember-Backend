from django.urls import path, include
from .views import LogsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', LogsView, basename='api.logs')

urlpatterns = [
    path('', include(router.urls))
]

