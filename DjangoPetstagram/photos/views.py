from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from DjangoPetstagram.common.forms import CommentForm
from DjangoPetstagram.common.utils import get_likes
from DjangoPetstagram.core.views_mixins import IsOwnerMixin, OwnerRequiredMixin
from DjangoPetstagram.photos.models import Photo


class AddPhoto(LoginRequiredMixin, views.CreateView):
    model = Photo
    template_name = 'photos/photo-add-page.html'
    fields = ('photo', 'description', 'location', 'tagged_pets')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.user = self.request.user
        form.save()
        return redirect('details_photo', pk=photo.id)



class DetailsPhoto(IsOwnerMixin, views.DetailView):
    template_name = 'photos/photo-details-page.html'
    model = Photo

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['is_owner'] = self.is_owner()
        data['photo'] = get_likes(data['photo'])
        data['form'] = CommentForm()
        return data


class EditPhoto(LoginRequiredMixin, OwnerRequiredMixin, views.UpdateView):
    model = Photo
    template_name = 'photos/photo-edit-page.html'
    fields = ('photo', 'description', 'location', 'tagged_pets')


    def get_success_url(self):
        return reverse_lazy('details_photo', kwargs={'pk': self.object.pk})


class DeletePhoto(LoginRequiredMixin, OwnerRequiredMixin, views.DeleteView):
    model = Photo
    template_name = 'photos/photo-delete-page.html'
    success_url = reverse_lazy('index')
