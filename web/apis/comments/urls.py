from django.urls import path, include
from .views import CommentView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('', CommentView, basename='api.comments')

urlpatterns = [
    path('', include(router.urls)),
]

