from django import forms

from DjangoPetstagram.common.models import PhotoComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...',
                    'maxlength': 300
                }
            )
        }


class SearchByPetForm(forms.Form):
    pet_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by pet name...'
            }
        )
    )
