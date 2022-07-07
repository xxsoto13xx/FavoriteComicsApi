from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .logic import access_token


def get_user_id(access_token):
    user_id = access_token['user_id']
    return user_id


class Authenticated(permissions.BasePermission):
    def has_permission(self):
        user_id = get_user_id(access_token)
        if user_id >= 1:
            return True
        else:
            return False
