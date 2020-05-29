from django.contrib import admin

# Register your models here.
from .models import Post, Author, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class PostAdmin(admin.ModelAdmin):
    pass
