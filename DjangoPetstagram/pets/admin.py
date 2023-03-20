from django.contrib import admin

from DjangoPetstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
   list_display = ('name', 'date_of_birth', 'slug')
