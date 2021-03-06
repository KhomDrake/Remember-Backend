from django.urls import path, include
from .views import TypeMemoryLineView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', TypeMemoryLineView, basename='api.type')

urlpatterns = [
    path('', include(router.urls))
]
