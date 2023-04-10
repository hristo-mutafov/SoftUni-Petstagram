from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from DjangoPetstagram.common.forms import CommentForm
from DjangoPetstagram.common.models import PhotoComment
from DjangoPetstagram.core.views_mixins import IsOwnerMixin, OwnerRequiredMixin
from DjangoPetstagram.pets.models import Pet


class AddPet(LoginRequiredMixin, views.CreateView):
    model = Pet
    template_name = 'pets/pet-add-page.html'
    fields = ('name', 'date_of_birth', 'personal_photo')


    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return redirect('details_pet', slug=pet.slug, username=self.request.user.username)


class DeletePet(LoginRequiredMixin, OwnerRequiredMixin, views.DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'

    def get_success_url(self):
        return reverse_lazy('detail_user', kwargs={'pk': self.request.user.id})


class DetailPet(IsOwnerMixin, views.DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['photos'] = self.object.photo_set.all()
        data['photo_count'] = self.object.photo_set.count()
        data['is_owner'] = self.is_owner()
        data['form'] = CommentForm()
        return data

class EditPet(LoginRequiredMixin, OwnerRequiredMixin, views.UpdateView):
    model = Pet
    template_name = 'pets/pet-edit-page.html'
    fields = ('name', 'date_of_birth', 'personal_photo')

    def get_success_url(self):
        return reverse_lazy('details_pet', kwargs={'username': self.request.user.username, 'slug': self.object.slug})
