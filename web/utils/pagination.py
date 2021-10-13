from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        data = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'current': self.request.query_params.get('page', None),
            'count': self.page.paginator.count,
            'results': data
        }

        return Response(data)
