from django.urls import path

from DjangoPetstagram.common.views import index, like, comment

urlpatterns = (
    path('', index, name='index'),
    path('like/<int:photo_id>/', like, name='like'),
    path('comment/<int:pk>', comment, name='comment')
)