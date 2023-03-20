from django.urls import path, include
from DjangoPetstagram.accounts.views import RegisterUser, LogOutUser, \
    LogInUser, DetailsUser, EditUser, DeleteUser

urlpatterns = (
    path('register/', RegisterUser.as_view(), name='register_user'),
    path('login/', LogInUser.as_view(), name='login_user'),
    path('logout/', LogOutUser.as_view(), name='logout_user'),
    path('profile/<int:pk>/', include([
        path('', DetailsUser.as_view(), name='detail_user'),
        path('delete/', DeleteUser.as_view(), name='delete_user'),
        path('edit/', EditUser.as_view(), name='edit_user')
    ])),
)