from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from DjangoPetstagram.core.model_mixins import StrRepresentationMixin

UserModel = get_user_model()

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

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        null=False,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        if not self.user:
            self.user = self.request.user

        super().save(*args, **kwargs)
