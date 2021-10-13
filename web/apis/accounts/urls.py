from django.urls import path, include
from .views import RememberAccountView, ActivateView
from .tokens import CustomJWTSerializer
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = SimpleRouter()
router.register('', RememberAccountView, basename='api.accounts')

urlpatterns = [
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="api.accounts.activate"),
    path('login/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='api.accounts.login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='api.accounts.login.refresh'),
    path('', include(router.urls))
]
