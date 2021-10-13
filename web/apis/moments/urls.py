from django.urls import path, include
from .views import MomentsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', MomentsView, basename='api.moments')

urlpatterns = [
    path('', include(router.urls)),
]

