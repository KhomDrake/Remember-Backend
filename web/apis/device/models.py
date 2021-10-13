import uuid
from django.db import models
from apis.accounts.models import RememberAccount

class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_id = models.CharField(unique=True, max_length=500)
    name = models.CharField(max_length=100)
    firebase_token = models.CharField(max_length=500)
    os_version = models.CharField(max_length=100)
    owner = models.ForeignKey(RememberAccount, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)