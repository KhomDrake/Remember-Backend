from django.urls import path, include
from .views import HistoryView, HistoryParticipantsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', HistoryView, basename='api.history')
router.register('participants', HistoryParticipantsView, basename='api.history')

urlpatterns = [
    path('', include(router.urls))
]

