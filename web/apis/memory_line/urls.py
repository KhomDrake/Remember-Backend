from django.urls import path, include
from .views import MemoryLineView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', MemoryLineView, basename='api.memory_line')

urlpatterns = [
    path('', include(router.urls))
]

