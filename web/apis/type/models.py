import uuid
from django.db import transaction
from django.db import models
from apis.accounts.models import RememberAccount

class Type(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    owners = models.ManyToManyField(
        RememberAccount, 
        through='type.TypeOwner',
        related_name="owners"
    )

    @transaction.atomic
    def add_type_owner(self, owner):
        hasType = TypeOwner.objects.filter(owner=owner, type=self)

        if(hasType.count() == 0):
            TypeOwner.objects.create(owner=owner, type=self, priority=1000)

    @staticmethod
    @transaction.atomic
    def create_type(name, owner):
        type = Type()
        type.name = name
        type.save()
        type.add_type_owner(owner)
        return type

class TypeOwner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    owner = models.ForeignKey(RememberAccount, on_delete=models.CASCADE)
    priority = models.IntegerField(default=1)