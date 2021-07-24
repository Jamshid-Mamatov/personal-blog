from django.contrib import admin
from .models import Post

class Post_admin(admin.ModelAdmin):
    list_display=("tittle",'text','author')

admin.site.register(Post,Post_admin)