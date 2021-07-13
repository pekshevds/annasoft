from django.contrib import admin

from .models import Section
from .models import Record


class RecordAdmin(admin.ModelAdmin):
	
	list_display = (
		'title',
		'customer',
		'section',
		)
	list_filter = ('customer', 'section')

admin.site.register(Record, RecordAdmin)

class SectionAdmin(admin.ModelAdmin):
	
	list_display = (
		'title',
		)

admin.site.register(Section, SectionAdmin)