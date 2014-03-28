from django.contrib import admin
from bpsc.reviews.models import Review, EnableUsersToSeeReview


def enable_reviews(modeladmin, request, queryset):
    queryset.update(access=True)

enable_reviews.short_description = 'Make reviews visible to public'


def disable_reviews(modeladmin, request, queryset):
    queryset.update(access=False)

disable_reviews.short_description = 'Make reviews hidden to public'


class EnableUsersToSeeReviewAdmin(admin.ModelAdmin):
    actions = [enable_reviews, disable_reviews]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        actions = super(EnableUsersToSeeReviewAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Review)
admin.site.register(EnableUsersToSeeReview, EnableUsersToSeeReviewAdmin)
