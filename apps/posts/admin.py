from django.contrib import admin

from .models import Tag, Category, Post


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category',
                    'featured', 'archived', 'posted_date']
    list_editable = ['featured', 'archived']
    list_filter = ['category', 'featured', 'archived']
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
