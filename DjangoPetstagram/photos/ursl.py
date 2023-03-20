from django.urls import path, include

from DjangoPetstagram.photos.views import AddPhoto, DetailsPhoto, EditPhoto, DeletePhoto

urlpatterns = (
    path('add/', AddPhoto.as_view(), name='add_photo'),
    path('<int:pk>/', include([
        path('', DetailsPhoto.as_view(), name='details_photo'),
        path('edit/', EditPhoto.as_view(), name='edit_photo'),
        path('delete/', DeletePhoto.as_view(), name='delete_photo')
    ])),

)
