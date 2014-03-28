from django.contrib import admin

from bpsc.static_pages.models import Post

class PostAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(PostAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Post, PostAdmin)
