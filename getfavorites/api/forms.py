from django import forms
from getfavorites.models import UserFavComics


class UserFavComicsForm(forms.ModelForm):

    class Meta:
        model = UserFavComics
        fields = '__all__'
