from django.contrib import admin

from DjangoPetstagram.common.models import PhotoComment


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    pass
