import uuid
from django.db import models
from apis.accounts.models import RememberAccount

class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    receiver = models.ForeignKey(RememberAccount, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=300, null=True, default=None)
    category = models.CharField(max_length=50, default="Default")
