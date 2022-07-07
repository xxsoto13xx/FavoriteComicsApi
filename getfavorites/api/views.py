from rest_framework.viewsets import ModelViewSet
from .permissions import Authenticated
from getfavorites.models import UserFavComics
from .serializers import UserFavComicsSerializer
from getfavorites.api.logic import access_token
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

user_id = access_token['user_id']


class GetComicsApiViewSet(ModelViewSet):
    queryset = UserFavComics.objects.filter(user_id=user_id)
    permission_classes = [AllowAny]
    serializer_class = UserFavComicsSerializer
    #authentication_classes = [JWTAuthentication]
    filterset_fields = ['added', 'characters', 'title']
    http_method_names = ['get']
