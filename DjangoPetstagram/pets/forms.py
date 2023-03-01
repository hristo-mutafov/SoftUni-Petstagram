from django import forms

from DjangoPetstagram.core.form_mixins import DisableFieldsMixin, RewriteSaveMethodForDeleteMixin
from DjangoPetstagram.pets.models import Pet


class BasePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_bird', 'personal_photo')

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Name'}
            ),
            'date_of_bird': forms.DateInput(
                attrs={'placeholder': 'mm/dd/yyyy',
                       'type': 'date'}
            ),
            'personal_photo': forms.TextInput(
                attrs={'placeholder': 'Link to image'}
                )
        }

        labels = {
            'name': 'Pet name',
            'date_of_bird': 'Date of birth',
            'personal_photo': 'Link to image'
        }
class AddPetForm(BasePetForm):
    pass


class EditPetForm(BasePetForm):
    pass




class DeletePetForm(DisableFieldsMixin, RewriteSaveMethodForDeleteMixin, BasePetForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly()



