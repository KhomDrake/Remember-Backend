from django.urls import path, include
from .views import TermView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', TermView, basename='api.terms')

urlpatterns = [
    path('', include(router.urls))
]
