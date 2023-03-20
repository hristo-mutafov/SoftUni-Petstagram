from django.urls import path, include

from DjangoPetstagram.pets.views import AddPet, DetailPet, EditPet, DeletePet

urlpatterns = (
    path('add/', AddPet.as_view(), name='add_pet'),
    path('<str:username>/pet/<slug:slug>/', include([
        path('', DetailPet.as_view(), name='details_pet'),
        path('delete/', DeletePet.as_view(), name='delete_pet'),
        path('edit/', EditPet.as_view(), name='edit_pet')
    ]))
)
