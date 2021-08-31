from django.contrib import admin

from .models import Profile, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass
    # search_fields = ['venue']
    # list_display = ['venue', 'created_date', 'date']
    # ordering = ['-created_date', ]


class ProfileAdmin(admin.ModelAdmin):
    pass
    # search_fields = ['venue']
    # list_display = ['venue', 'created_date', 'date']
    # ordering = ['-created_date', ]


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
