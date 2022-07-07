from django.db import models

# Create your models here.


class UserFavComics(models.Model):
    user_id = models.IntegerField(primary_key=True)
    comic_id = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.URLField()
    onsaledate = models.DateField()
    characters = models.TextField(blank=True, null=True)
    added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
