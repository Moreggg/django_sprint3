from django.contrib import admin
from .models import Post, Location, Category


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(Post, PostAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)
