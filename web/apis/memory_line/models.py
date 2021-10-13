import uuid

from django.db import models
from django.db import transaction
from guardian.shortcuts import assign_perm, remove_perm
from apis.accounts.models import RememberAccount
from apis.type.models import Type
from rest_framework.exceptions import NotFound

class MemoryLine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(RememberAccount, on_delete=models.CASCADE)
    participants = models.ManyToManyField(RememberAccount, through='memory_line.MemoryLineParticipants',
                                          related_name="participants")
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('send_invite', 'Send Invite'),
        )

    @staticmethod
    @transaction.atomic
    def create_memory_line(title, description, type, owner):
        memory_line = MemoryLine()
        memory_line.title = title
        memory_line.description = description
        memory_line.type = type
        memory_line.owner = owner
        memory_line.save()
        assign_perm('view_memoryline', owner, memory_line)
        assign_perm('delete_memoryline', owner, memory_line)
        assign_perm('change_memoryline', owner, memory_line)
        return memory_line

    @transaction.atomic
    def add_participant(self, participant):
        MemoryLineParticipants.objects.create(participant=participant, memory_line=self)
        assign_perm('view_memoryline', participant, self)
        assign_perm('send_invite', participant, self)

    @transaction.atomic
    def leave_memory_line(self, remember_account):
        try:
            MemoryLineParticipants.objects.get(participant=remember_account, memory_line=self).delete()
            remove_perm('view_memoryline', remember_account, self)
            remove_perm('send_invite', remember_account, self)
        except MemoryLineParticipants.DoesNotExist:
            raise NotFound(detail="Participant does not exist", code="does_not_exist")


class MemoryLineParticipants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participant = models.ForeignKey(RememberAccount, on_delete=models.CASCADE)
    memory_line = models.ForeignKey(MemoryLine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)




