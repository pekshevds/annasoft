from django.contrib import admin

from .models import (
    Category,
    Service,
    Article,
    Pages,
    CompanyContactData,
    Goods,
    MailingRecipients
)

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


class PagesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'meta_title',
    )
    search_fields = ('title',)       


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Pages, PagesAdmin)
admin.site.register(CompanyContactData)
admin.site.register(Goods)
admin.site.register(MailingRecipients)