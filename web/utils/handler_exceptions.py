from rest_framework.exceptions import ValidationError, APIException, AuthenticationFailed
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # check that a ValidationError exception is raised
    if isinstance(exc, ValidationError):
        response.data = {'error_type': 'validation_error',
                         'error_body': exc.get_full_details()
                         }
    elif isinstance(exc, AuthenticationFailed):
        response.data = {'error_type': 'authentication_failed',
                         'error_body': exc.get_full_details()
                         }

    elif isinstance(exc, APIException):
        response.data = {'error_type': exc.get_codes(),
                         'error_body': {'message': exc.detail}}

    return response

