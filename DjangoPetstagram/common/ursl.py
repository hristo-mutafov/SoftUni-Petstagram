from django.urls import path

from DjangoPetstagram.common.views import Index, like, comment

urlpatterns = (
    path('', Index.as_view(), name='index'),
    path('like/<int:photo_id>/', like, name='like'),
    path('comment/<int:pk>', comment, name='comment')
)
