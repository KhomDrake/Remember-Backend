from django.urls import path, include
from .views import InviteView
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('', InviteView, basename='api.invite')

urlpatterns = [
    path('', include(router.urls))
]
