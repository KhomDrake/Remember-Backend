from rest_framework import status
from rest_framework.response import Response

class RememberResponse:
    def __init__(self, status_code = status.HTTP_200_OK, data = None, success = True, error = None):
        self.body = {
            "success": success,
            "data": data,
            "error": error
        }
        self.statusCode = status_code
        
    def status(self, status_code):
        self.statusCode = status_code
        return self

    def ok(self):
        self.statusCode = status.HTTP_200_OK
        return self

    def no_content(self):
        self.statusCode = status.HTTP_204_NO_CONTENT
        return self

    def bad_request(self):
        self.set_success(False)
        self.statusCode = status.HTTP_400_BAD_REQUEST
        return self

    def unauthorized(self):
        self.statusCode = status.HTTP_401_UNAUTHORIZED
        self.set_success(False)
        self.set_error("UNAUTHORIZED", "Token não enviado ou inválido")
        return self

    def set_data(self, data):
        self.body["data"] = data
        return self

    def set_error(self, errorType, errorMessage, errorBody = None):
        self.body["error"] = {
            'errorType': errorType,
            'errorMessage': errorMessage,
            'errorBody': errorBody
        }
        return self

    def set_success(self, success = True):
        self.body["success"] = success
        return self

    def build(self):
        return Response(data=self.body, status=self.statusCode)