from rest_framework import serializers
from getfavorites.models import UserFavComics


class UserFavComicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavComics
        fields = ['user_id', 'comic_id', 'title', 'image',
                  'onsaledate', 'characters', 'added']
