from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views import generic as views

from DjangoPetstagram.accounts.forms import AppRegisterForm, EditUserProfileForm
from DjangoPetstagram.accounts.models import UserProfile
from DjangoPetstagram.core.views_mixins import OwnerRequiredMixin

user_model = get_user_model()

class RegisterUser(views.CreateView):
    template_name = 'accounts/register-page.html'
    model = user_model
    form_class = AppRegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        data = super().form_valid(form)
        login(self.request, self.object)
        return data

class LogInUser(LoginView):
    template_name = 'accounts/login-page.html'


class LogOutUser(LogoutView):
    pass



class DeleteUser(LoginRequiredMixin, OwnerRequiredMixin, views.DeleteView):
    model = user_model
    template_name = 'accounts/profile-delete-page.html'
    success_url = reverse_lazy('index')
    auth = True


class DetailsUser(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = user_model

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['is_owner'] = self.object.pk == self.request.user.pk
        data['pets'] = self.object.pet_set.all()
        data['profile'] = self.object.userprofile
        data['photos'] = self.object.photo_set.prefetch_related('photolike_set')
        data['likes'] = sum(photo.photolike_set.count() for photo in data['photos'])

        return data


class EditUser(LoginRequiredMixin, OwnerRequiredMixin, views.UpdateView):
    model = UserProfile
    template_name = 'accounts/profile-edit-page.html'
    form_class = EditUserProfileForm

    def get_success_url(self):
        return reverse_lazy('detail_user', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data['instance'].email = data['instance'].user.email
        return data

    def form_valid(self, form):
        super().form_valid(form)
        self.object.user.email = form.data['email']
        self.object.user.save()
        return super().form_valid(form)



