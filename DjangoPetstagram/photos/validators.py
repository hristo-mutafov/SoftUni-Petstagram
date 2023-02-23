from django.core.exceptions import ValidationError

from DjangoPetstagram.core.utils import bytes_to_mb


def check_file_size_5mb(photo):
    photo_size = photo.file.size
    mb_limit = 5.0
    if photo_size > bytes_to_mb(mb_limit):
        raise ValidationError('The file size is over 5mb')