from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.utils.text import slugify

from DjangoPetstagram.core.model_mixins import StrRepresentationMixin


class Pet(StrRepresentationMixin, models.Model):
    repr_columns = ('name',)
    MAX_NAME_LENGTH = 30
    MIN_NAME_LENGTH = 2
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        validators=(MinLengthValidator(MIN_NAME_LENGTH),)
    )
    personal_photo = models.URLField(
        null=False,
        blank=False
    )
    date_of_bird = models.DateField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        null=False,
        blank=True
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Create the obj

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}') # Use the attributes of the created obj

        super().save(*args, **kwargs)  # Save the changes
