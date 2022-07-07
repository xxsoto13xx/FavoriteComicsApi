from rest_framework.viewsets import ModelViewSet
from getfavorites.models import UserFavComics
from getfavorites.api.serializers import UserFavComicsSerializer
from .permissions import IsAuthenticatedandComicExist
from rest_framework_simplejwt.authentication import JWTAuthentication


class AddComicsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedandComicExist]
    serializer_class = UserFavComicsSerializer
    authentication_classes = [JWTAuthentication]
    http_method_names = ['post']
