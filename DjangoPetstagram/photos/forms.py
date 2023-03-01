from django import forms

from DjangoPetstagram.core.form_mixins import DisableFieldsMixin, RewriteSaveMethodForDeleteMixin
from DjangoPetstagram.photos.models import Photo


class BasePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description', 'location', 'tagged_pets']
        labels = {
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tag Pets'
        }

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']
        labels = {
            'photo': 'Photo',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tag Pets'
        }

class EditPhotoForm(BasePhotoForm):
    pass

class DeletePhotoForm(DisableFieldsMixin, RewriteSaveMethodForDeleteMixin, BasePhotoForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly()

