from DjangoPetstagram.common.models import PhotoLike, PhotoComment


class DisableFieldsMixin:
    disabled_fields = ()
    final_fields = {}

    def _apply_readonly(self):
        if self.disabled_fields == '__all__':
            self.final_fields = self.fields.keys()
        else:
            self.final_fields = self.disabled_fields

        for field_name in self.final_fields:
            if field_name in self.fields:
                field = self.fields[field_name]
                field.widget.attrs['readonly'] = 'readonly'



class RewriteSaveMethodForDeleteMixin:
    def save(self, commit=True):
        if commit:
            if self.instance.__class__.__name__ == 'Photo':
                self.instance.tagged_pets.clear()
                PhotoLike.objects.filter(photo=self.instance.id).delete()
                PhotoComment.objects.filter(photo=self.instance.id).delete()
            self.instance.delete()

        return self.instance




