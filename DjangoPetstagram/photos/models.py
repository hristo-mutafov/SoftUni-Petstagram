from django.core.validators import MinLengthValidator
from django.db import models

from DjangoPetstagram.core.model_mixins import StrRepresentationMixin
from DjangoPetstagram.pets.models import Pet
from DjangoPetstagram.photos.validators import check_file_size_5mb


class Photo(StrRepresentationMixin, models.Model):
    class Meta:
        ordering = ('photo', )

    repr_columns = ('id', 'description')
    MAX_DESC_LEN = 300
    MIN_DESC_LEN = 10
    MAX_LOCATION_LEN = 30
    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to='media_files/photo_app',
        validators=(check_file_size_5mb,)
    )

    description = models.CharField(
        max_length=MAX_DESC_LEN,
        blank=True,
        null=True,
        validators=(MinLengthValidator(MIN_DESC_LEN),)
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LEN,
        null=False,
        blank=False
    )

    date_of_publication = models.DateField(
        auto_now=True,
        null=False,
        blank=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True
    )
