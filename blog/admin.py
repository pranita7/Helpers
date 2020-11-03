from django.contrib import admin

# Register your models here.
from blog.models import Post, Images
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    list_filter = ['created', 'updated']
    search_fields = ['author__username']
    # date_hierarchy = 'created'

class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

admin.site.register(Post, PostAdmin)
admin.site.register(Images, ImagesAdmin)