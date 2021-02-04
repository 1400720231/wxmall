import jwt
from django.utils.encoding import smart_text
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class JSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    """
    

    """
    www_authenticate_realm = 'api'

    def get_jwt_value(self, request):
        auth = get_authorization_header(request)

        if not auth:
            return None
        return auth
