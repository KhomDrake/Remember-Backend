import uuid
from django.db import models, transaction
from guardian.shortcuts import assign_perm

from ..accounts.models import User
from ..memory_line.models import MemoryLine


class Invite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guest')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    memory_line = models.ForeignKey(MemoryLine, on_delete=models.CASCADE)
    answered = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    @staticmethod
    @transaction.atomic
    def create_invite(guest, owner, memory_line):
        invite = Invite(memory_line=memory_line, guest=guest, owner=owner)
        invite.save()
        assign_perm('view_invite', guest, invite)
        assign_perm('view_invite', owner, invite)
        return invite
