import admin_thumbnails
from django.contrib import admin
from posts.models import *

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail('photo')
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "content",
    ]
    inlines = [
        CommentInline,
        PostImageInline,
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'post',
        'photo',
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'post',
        'content',
    ]

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    name = models.CharField('태그명', max_length=50)

    def __str__(self):
        return self.name