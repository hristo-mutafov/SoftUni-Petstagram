from django.contrib.auth import get_user_model
from django.db import models

from DjangoPetstagram.photos.models import Photo

UserModel = get_user_model()

class PhotoComment(models.Model):

    class Meta:
        ordering = ['-date_of_publication']


    MAX_TEXT_LEN = 300
    text = models.CharField(
        max_length=MAX_TEXT_LEN,
        null=False,
        blank=False
    )
    date_of_publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False
    )
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )

