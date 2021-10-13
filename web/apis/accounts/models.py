import uuid

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, models
from phonenumber_field.modelfields import PhoneNumberField

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .choices import STATE_CHOICES


class User(AbstractUser):
    """
    Override Abstract default User
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default="")
    nickname = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    is_remember_account = models.BooleanField(default=False)
    country = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=80, blank=True)
    ur = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [name, email, nickname]


class RememberAccount(User):
    """
    User RememberAccount
    """
    photo = models.ImageField(null=True, upload_to='photos')
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    accept_terms = models.BooleanField(default=False)
    
    @staticmethod
    def create_account(username, password, email, **kwargs):
        remember_account = RememberAccount()
        remember_account.username = username
        remember_account.password = make_password(password)
        remember_account.email = email
        remember_account.is_remember_account = True
        remember_account.name = kwargs.get("name")
        remember_account.photo = kwargs.get("photo")
        remember_account.nickname = kwargs.get("nickname")
        remember_account.bio = kwargs.get("bio")
        remember_account.birth_date = kwargs.get("birth_date")
        remember_account.gender = kwargs.get("gender")
        remember_account.save()
        return remember_account

    def confirmation_email(self, request):
        from .tokens import account_activation_token
        domain = request.get_host()
        mail_subject = 'Activate your Remember account.'
        html_content = render_to_string('accounts/email/email_confirmation.html', {
            'user': self,
            'domain': domain,
            'uidb64': urlsafe_base64_encode(force_bytes(self.pk)),
            'token': account_activation_token.make_token(self),
        })
        message = strip_tags(html_content)
        from_email = settings.DEFAULT_ACCOUNT_EMAIL
        to_email = self.email
        email = EmailMultiAlternatives(
            mail_subject, message, from_email, to=[to_email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()




