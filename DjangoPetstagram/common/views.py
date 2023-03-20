from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views import generic as views

from DjangoPetstagram.common.forms import CommentForm, SearchByPetForm
from DjangoPetstagram.common.models import PhotoLike, PhotoComment
from DjangoPetstagram.common.utils import get_likes, check_if_liked, get_photo_by_id
from DjangoPetstagram.photos.models import Photo


class Index(views.ListView):
    model = Photo
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # Filtering
        photos = None
        search_form = SearchByPetForm(self.request.GET)
        search_form.is_valid()
        if search_form.cleaned_data['pet_name']:
            filter_by = search_form.cleaned_data['pet_name']
            photos = self.object_list.filter(tagged_pets__name__icontains=filter_by).all()
        else:
            photos = self.object_list

        photos = [get_likes(photo) for photo in photos]
        photos = [check_if_liked(photo) for photo in photos]

        data['photos'] = photos
        data['form'] = CommentForm()
        data['comment'] = PhotoComment.objects.first()
        data['search_form'] = search_form

        return data


@login_required
def like(request, photo_id):
    photo = get_photo_by_id(photo_id)
    present = [photo_like for photo_like in photo.photolike_set.all() if photo_like.user == request.user]
    if present:
        [obj.delete() for obj in present]
    else:
        PhotoLike.objects.create(
            photo=photo,
            user=request.user
        )

    return redirect(f'/#{photo.pk}')


@login_required
def comment(request, pk):
    photo = get_photo_by_id(pk)

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.user = request.user
        comment.save()
    return redirect('details_photo', pk=pk)


