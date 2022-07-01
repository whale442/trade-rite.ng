from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'author','title', 'slug', 'date_posted', 'datedate_updated']
    list_filter = ['date_posted','datedate_updated']
    list_editable = ['title',]
    prepopulated_fields = {'slug':('title',)}