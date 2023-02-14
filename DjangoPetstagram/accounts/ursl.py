from django.urls import path, include
from DjangoPetstagram.accounts.views import delete_user, details_user, edit_user, register_user, login_user

urlpatterns = (
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('profile/<int:pk>/', include([
        path('', details_user, name='detail_user'),
        path('delete/', delete_user, name='delete_user'),
        path('edit/', edit_user, name='edit_user')
    ])),
)