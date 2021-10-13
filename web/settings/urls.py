"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view
from rest_framework.permissions import AllowAny
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="RememberCore API",
        default_version='v1',
        description="Documentação dos endpoints da Remembercore API",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@sophier.com.br"),
        license=openapi.License(name="BSD License")
    ),
    url=settings.SWAGGER_METHODS_URL,
    public=True,
    permission_classes=(AllowAny,)
)


urlpatterns = [
    path('', RedirectView.as_view(url='api/v1/', permanent=False), name='index'),
    path('api/v1/accounts/', include('apis.accounts.urls')),
    path('api/v1/memory-lines/', include('apis.memory_line.urls')),
    path('api/v1/moments/', include('apis.moments.urls')),
    path('api/v1/comments/', include('apis.comments.urls')),
    path('api/v1/invites/', include('apis.invite.urls')),
    path('api/v1/history/', include('apis.history.urls')),
    path('api/v1/type/', include('apis.type.urls')),
    path('api/v1/notification/', include('apis.notification.urls')),
    path('api/v1/logs/', include('apis.logs.urls')),
    path('api/v1/terms/', include('apis.terms.urls')),
    path('api/v1/device/', include('apis.device.urls')),
    path('api/v1/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
