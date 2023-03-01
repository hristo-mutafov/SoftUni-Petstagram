from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from DjangoPetstagram import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DjangoPetstagram.common.ursl')),
    path('accounts/', include('DjangoPetstagram.accounts.ursl')),
    path('pets/', include('DjangoPetstagram.pets.ursl')),
    path('photos/', include('DjangoPetstagram.photos.ursl'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

