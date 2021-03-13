from django.contrib import admin

from .models import Person
from .models import Customer
from .models import Employee
from .models import Position
from .models import Task
from .models import Record

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
	list_display = (		
		'first_name',
		'middle_name',
		'last_name',
		'birthdate',
		'sex',
	)
		
	list_filter = ( 'sex', )


class EmployeeInline(admin.TabularInline):
    model = Employee    
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
	list_display = (		
		'name',
		'inn',
		'kpp',		
	)
		
	search_fields = ('name', 'inn',)
	list_filter = ( 'kpp', )
	inlines = [EmployeeInline, ]


class TaskAdmin(admin.ModelAdmin):
	list_display = (	
		'__str__',
		'task_status',
		'customer',
		'performer',		
	)
		
	list_filter = ( 'task_status', )


class RecordAdmin(admin.ModelAdmin):
	list_display = (	
		'id',
		'date',
		'task',
		'task_status',
		'user',		
	)
		
	list_filter = ( 'user', )
	
	

admin.site.register(Person, PersonAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Position)
admin.site.register(Task, TaskAdmin)
admin.site.register(Record, RecordAdmin)