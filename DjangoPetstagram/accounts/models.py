import enum

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core import validators

from django.db import models

from DjangoPetstagram.accounts.validators import check_alphabetical_letters
from DjangoPetstagram.core.model_mixins import GetEnumValuesMixin, GetEnumMaxLenValueMixin
from DjangoPetstagram.photos.validators import check_file_size_5mb


class GenderEnum(GetEnumValuesMixin, GetEnumMaxLenValueMixin, enum.Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'



class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 150
    USERNAME_FIELD = 'username'
    objects = UserManager()

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
        null=False,
        blank=False,

    )

    email = models.EmailField(
        "email address",
        unique=True,
        null=False,
        blank=False,
        )

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    date_joined = models.DateTimeField("date joined", auto_now_add=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not UserProfile.objects.filter(user_id=self.id):
            profile = UserProfile(
                user=self,
                gender=GenderEnum.DoNotShow.value
            )
            profile.save()
        return super().save(*args, **kwargs)


class UserProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    user_model = get_user_model()

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH), check_alphabetical_letters),
        null=False,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(validators.MinLengthValidator(LAST_NAME_MIN_LENGTH), check_alphabetical_letters),
        null=False,
        blank=True,
    )

    gender = models.CharField(
        max_length=GenderEnum.max_length(),
        choices=GenderEnum.get_values(),
        null=False,
        blank=True,
        default=GenderEnum.DoNotShow,
    )

    profile_picture = models.ImageField(
        upload_to='media_files/accounts_app',
        validators=(check_file_size_5mb,),
        blank=True
    )

    user = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        primary_key=True
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
