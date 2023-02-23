from django.urls import path

from DjangoPetstagram.common.views import index, like

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like, name='like'),
)