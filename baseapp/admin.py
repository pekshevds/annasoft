from django.contrib import admin

from .models import Category
from .models import Service
from .models import Article

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    search_fields = ('name',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id',
    )

    search_fields = ('title',)    


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'category',
    )

    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Article, ArticleAdmin)