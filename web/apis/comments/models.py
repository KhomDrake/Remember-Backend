import uuid

from django.db import models, transaction
from apis.accounts.models import RememberAccount
from apis.moments.models import Moment
from guardian.shortcuts import assign_perm

# Create your models here.
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    owner = models.ForeignKey(RememberAccount, on_delete=models.DO_NOTHING)
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    @transaction.atomic
    def create_moment(owner, moment, **kwargs):
        comment = Comment()
        comment.owner = owner
        comment.moment = moment
        comment.content = kwargs.get("content")
        comment.save()
        assign_perm('delete_comment', owner, comment)
        assign_perm('change_comment', owner, comment)
        return comment

