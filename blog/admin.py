from django.contrib import admin

from .models import posts, Blog, Comment

admin.site.register(posts)
admin.site.register(Blog)
admin.site.register(Comment)
