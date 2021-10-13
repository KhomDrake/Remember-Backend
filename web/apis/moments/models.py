import uuid

from django.db import models, transaction
from guardian.shortcuts import assign_perm

from apis.accounts.models import RememberAccount
from apis.memory_line.models import MemoryLine


class Moment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='moments', null=True)
    owner = models.ForeignKey(RememberAccount, on_delete=models.DO_NOTHING)
    memory_line = models.ForeignKey(MemoryLine, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    @transaction.atomic
    def create_moment(owner, memory_line, **kwargs):
        moment = Moment()
        moment.owner = owner
        moment.memory_line = memory_line
        moment.file = kwargs.get("file")
        moment.description = kwargs.get("description")
        moment.save()
        assign_perm('delete_moment', owner, moment)
        assign_perm('change_moment', owner, moment)
        return moment

