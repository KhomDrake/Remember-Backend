from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .tokens import account_activation_token


class RememberAccountView(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    """
    Create, Update and List Users
    """
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'name', 'nickname']
    serializer_class = RememberAccountSerializer
    authentication_classes = (JWTAuthentication,)
    parser_classes = (JSONParser,)

    def get_authenticators(self):
        if self.request.method == 'POST':
            self.authentication_classes = []
        return super(RememberAccountView, self).get_authenticators()


    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return RememberAccount.objects.none()
        if self.action == 'me':
            return RememberAccount.objects.get(is_active=True, email=self.request.user.email)
        return RememberAccount.objects.filter(is_active=True)

    def perform_create(self, serializer):
        account = serializer.save()
        account.confirmation_email(self.request)


    @action(detail=False, methods=['get'], permission_classes=(IsAuthenticated,))
    def me(self, request):
        """
        Get Account
        """
        serializer = self.get_serializer(self.get_queryset())
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], authentication_classes = [], serializer_class=VerifyEmailSerializer, permission_classes=(AllowAny,))
    def verify_email(self, request):
        """
        Get Account
        """
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        if not RememberAccount.objects.filter(email=email).exists():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], authentication_classes = [], serializer_class=VerifyUsernameSerializer, permission_classes=(AllowAny,))
    def verify_username(self, request):
        """
        Get Account
        """
        serializer = VerifyUsernameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        if not RememberAccount.objects.filter(username=username).exists():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['patch'], url_path='terms/accept', permission_classes=(IsAuthenticated,))
    def accept_terms(self, request):
        query = RememberAccount.objects.get(is_active=True, email=self.request.user.email)

        if query.accept_terms == True:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.data = {
                'error_type': 'already_accept_terms',
                'error_body': []
            }
            return response

        query.accept_terms = True
        query.save()
        return Response(status=status.HTTP_200_OK)

class ActivateView(APIView):
    permission_classes = [AllowAny]
    queryset = User.objects.filter(is_active=False)

    def get(self, request, uidb64, token):
        """
        Activate a User
        """
        uid = force_text(urlsafe_base64_decode(uidb64))
        try:
            user = self.queryset.get(pk=uid)
        except self.queryset.model.DoesNotExist:
            raise NotFound(detail="User does not exist", code="does_not_exist")
        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'Message': 'Email validated successfully!!!'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


