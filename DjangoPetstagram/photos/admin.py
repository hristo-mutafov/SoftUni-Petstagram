from django.contrib import admin

from DjangoPetstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('description', 'location', 'pets')

    def pets(self, photo_obj):
        return ', '.join(pet.name for pet in photo_obj.tagged_pets.all())
