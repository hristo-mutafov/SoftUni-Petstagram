
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DjangoPetstagram.common.ursl')),
    path('accounts/', include('DjangoPetstagram.accounts.ursl')),
    path('pets/', include('DjangoPetstagram.pets.ursl')),
    path('photos/', include('DjangoPetstagram.photos.ursl'))
]
