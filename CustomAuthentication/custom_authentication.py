from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed


class CustomBaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username=User.objects.get('username')
        if username is None:
            return None

        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('User Not Found...')
        
        return (user,None)