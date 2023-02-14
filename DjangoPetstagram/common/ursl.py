from django.urls import path

from DjangoPetstagram.common.views import index

urlpatterns = (
    path('', index, name='index'),
)