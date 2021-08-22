from authentication.models import MyUser
from rest_framework import authentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated

class MyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = authentication.get_authorization_header(request)
        auth = auth.decode('utf-8').split(" ")

        print(auth)
        if not auth or auth[0].lower() != 'bearer':
            msg = _('Invalid token header. Need to be Bearer')
            raise exceptions.AuthenticationFailed(msg)
        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)
        
        try:
            token = auth[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            print(payload)
            if not payload['email']:
                msg = _('Invalid token header. Email field is not provided in the token')
                raise exceptions.AuthenticationFailed(msg)
            user = MyUser.objects.get(email=payload['email'])
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)
        except MyUser.DoesNotExist:
            msg = _('Invalid token header. No such user')
            raise exceptions.AuthenticationFailed(msg)
            
        except jwt.ExpiredSignatureError as ex:
            raise exceptions.AuthenticationFailed(
                'Token is expired, login again')

        except jwt.DecodeError as ex:
            raise exceptions.AuthenticationFailed(
                'Token is invalid,')
        print((user, token))
        return (user, token)


class MyCustomPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return super().has_permission(request, view)

class MyCustomAuthentication(MyAuthentication):
    def authenticate(self, request):
        print(request.method)
        if request.method == 'POST':
            print('in if clause')
            pass
        else:
            print('in else clause')
            return super().authenticate(request)