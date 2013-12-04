from django.contrib import admin
from bpsc.wysiwyg.models import Post

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('name', 'url')

admin.site.register(Post, PostAdmin)