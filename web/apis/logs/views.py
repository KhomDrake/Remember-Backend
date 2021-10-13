from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets
from ..invite.models import Invite
from ..invite.serializers import InviteSerializer
from ..accounts.models import RememberAccount
from ..accounts.serializers import RememberAccountSerializer
from ..comments.models import Comment
from ..comments.serializers import CommentSerializer
from ..memory_line.models import MemoryLine
from ..memory_line.serializers import MemoryLineSerializer
from ..moments.models import Moment
from ..moments.serializers import MomentsSerializer
from ..type.models import Type
from ..type.serializers import MemoryLineTypeOwnerSerializer

class LogsView(viewsets.ViewSet):
    def list(self, request, pk=None):
        invites = InviteSerializer(data=Invite.objects.all(), many=True)
        invites.is_valid()
        accounts = RememberAccountSerializer(data=RememberAccount.objects.all(), many=True)
        accounts.is_valid()
        comments = CommentSerializer(data=Comment.objects.all(), many=True)
        comments.is_valid()
        memoryLine = MemoryLineSerializer(data=MemoryLine.objects.all(), many=True)
        memoryLine.is_valid()
        moments = MomentsSerializer(data=Moment.objects.all(), many=True)
        moments.is_valid()
        types = MemoryLineTypeOwnerSerializer(data=Type.objects.all(), many=True)
        types.is_valid()
        body = {
            "memory_lines": len(memoryLine.data),
            "moments": len(moments.data),
            "comments": len(comments.data),
            "users": len(accounts.data),
            "invites": len(invites.data),
            "type": len(types.data)
        }
        return Response(body, status=status.HTTP_200_OK)