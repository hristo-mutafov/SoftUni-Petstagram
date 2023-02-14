from django.urls import path, include

from DjangoPetstagram.pets.views import add_pet, delete_pet, details_pet, edit_pet

urlpatterns = (
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', details_pet, name='details_pet'),
        path('delete/', delete_pet, name='delete_pet'),
        path('edit/', edit_pet, name='edit_pet')
    ]))
)