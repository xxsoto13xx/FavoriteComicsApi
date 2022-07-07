from logging import raiseExceptions
from rest_framework.permissions import BasePermission
from rest_framework import permissions
from getfavorites.api.logic import comics_id
from getfavorites.api.logic import access_token


class IsAuthenticatedandComicExist(permissions.BasePermission):
    def has_permission(self, request, view):
        comic_id = view.kwargs.get('comic_id', None)
        if comic_id in comics_id:
            return True
        else:
            return False
