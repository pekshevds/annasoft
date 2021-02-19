from django.shortcuts import render
from django.shortcuts import redirect

from baseapp.core import get_context

from .models import Customer
from .models import Employee
from .models import Task
from .models import Person
from .models import Position

from .core import get_tasks
from .core import send_task_to_B
from .core import send_task_to_C
from .core import send_task_to_D
from .core import get_default_performer

from .core import create_new_task
from .core import update_task

from .core import create_new_customer
from .core import update_customer

from .core import create_new_person
from .core import update_person

from .core import create_new_employee
from .core import update_employee

from datetime import datetime

# Create your views here.
def show_index(request):

	context = get_context()	
	return render(request, "crmapp/index.html", context)


def show_canban(request):

	context = get_context()
	context['tasks_A'] = get_tasks("A")
	context['tasks_B'] = get_tasks("B")
	context['tasks_C'] = get_tasks("C")
	return render(request, "crmapp/canban.html", context)


def send_to_B(request, id):

	send_task_to_B(id)
	return redirect('show-canban')


def send_to_C(request, id):

	send_task_to_C(id)
	return redirect('show-canban')


def send_to_D(request, id):

	send_task_to_D(id)
	return redirect('show-canban')


def save_task(request):

	id = int(request.POST.get("id", "0"))
	customer_id = request.POST.get("customer", "0")
	from_customer_id = request.POST.get("from_customer", "0")
	performer_id = request.POST.get("performer", "0")
	from_performer_id = request.POST.get("from_performer", "0")
	dead_line = datetime.strptime(request.POST.get("dead_line", ""), "%Y-%m-%d")
	description = request.POST.get("description", "")

	customer = Customer.objects.filter(id=customer_id).first()
	from_customer = Employee.objects.filter(id=from_customer_id).first()

	performer = Customer.objects.filter(id=performer_id).first()
	from_performer = Employee.objects.filter(id=from_performer_id).first()


	time_scheduled_h = int(request.POST.get("time_scheduled_h", "0"))
	time_scheduled_m = int(request.POST.get("time_scheduled_m", "0"))
	time_actual_h = int(request.POST.get("time_actual_h", "0"))
	time_actual_m = int(request.POST.get("time_actual_m", "0"))

	

	if id == 0:

		if create_new_task(customer=customer, 
			from_customer=from_performer, 
			performer=performer, 
			from_performer=from_performer, 
			dead_line=dead_line, 
			description=description,
			time_scheduled_h=time_scheduled_h,
			time_scheduled_m=time_scheduled_m,
			time_actual_h=time_actual_h,
			time_actual_m=time_actual_m):
			return redirect('show-canban')
	else:

		if update_task(task=Task.objects.get(id=id),
			customer=customer, 
			from_customer=from_performer, 
			performer=performer, 
			from_performer=from_performer, 
			dead_line=dead_line, 
			description=description,
			time_scheduled_h=time_scheduled_h,
			time_scheduled_m=time_scheduled_m,
			time_actual_h=time_actual_h,
			time_actual_m=time_actual_m):
			return redirect('show-canban')

	return redirect(request.META['HTTP_REFERER'])
	


def show_task(request, id):
	
	context = get_context()
	
	context['id'] = 0
	context['task'] = None
	context['customer'] = None
	context['from_customer'] = None
	context['performer'] = None
	context['from_performer'] = None
	context['dead_line'] = None
	context['description'] = ''	

	if id > 0:
		context['task'] = Task.objects.get(id=id)
		context['id'] = context['task'].id 
		context['customer'] = context['task'].customer
		context['from_customer'] = context['task'].from_customer 
		context['performer'] = context['task'].performer 
		context['from_performer'] = context['task'].from_performer 
		context['dead_line'] = context['task'].dead_line.strftime("%Y-%m-%d") 		
		context['description'] = context['task'].description 

	return render(request, "crmapp/task.html", context)


def new_task(request, customer_id):
	
	context = get_context()	
	context['id'] = 0
	context['customer'] = Customer.objects.get(id=customer_id)
	context['performer'] = get_default_performer()

	return render(request, "crmapp/task.html", context)


def show_persons(request):
	
	context = get_context()
	context['persons'] = Person.objects.all()
	return render(request, "crmapp/persons.html", context)


def new_person(request):

	context = get_context()		
	context['person'] = None

	return render(request, "crmapp/person.html", context)


def show_person(request, id):
	
	context = get_context()		
	context['person'] = Person.objects.get(id=id)
	return render(request, "crmapp/person.html", context)


def save_person(request):

	id = int(request.POST.get('id', "0"))
	first_name = request.POST.get('first_name', '')
	middle_name = request.POST.get('middle_name', '')
	last_name = request.POST.get('last_name', '')
	

	birthdate = datetime.strptime(request.POST.get('birthdate', None), '%Y-%m-%d')
	sex = request.POST.get('sex', '')
	email = request.POST.get('email', '')
	address1 = request.POST.get('address1', '')
	address2 = request.POST.get('address2', '')
	phone1 = request.POST.get('phone1', '')
	phone2 = request.POST.get('phone2', '')
	description = request.POST.get('description', '')

	if id == 0:

		if create_new_person(first_name=first_name, 
			middle_name=middle_name, 
			last_name=last_name, 
			birthdate=birthdate, 
			sex=sex,
			email=email,
			address1=address1,
			address2=address2,
			phone1=phone1,
			phone2=phone2,
			description=description):
			return redirect('show-crm-index')
	else:

		if update_person(person=Person.objects.get(id=id),
			first_name=first_name, 
			middle_name=middle_name, 			
			last_name=last_name, 
			birthdate=birthdate, 
			sex=sex,
			email=email,
			address1=address1,
			address2=address2,
			phone1=phone1,
			phone2=phone2,
			description=description):
			return redirect('show-crm-index')

	return redirect(request.META['HTTP_REFERER'])


def show_customers(request):
	
	context = get_context()
	context['customers'] = Customer.objects.all()
	return render(request, "crmapp/customers.html", context)


def show_customer(request, id):

	context = get_context()
	
	context['id'] = 0
	context['customer'] = None
	context['name'] = ''
	context['full_name'] = ''
	context['inn'] = ''
	context['kpp'] = ''
	context['email'] = ''
	context['address1'] = '' 
	context['address2'] = ''
	context['phone1'] = ''
	context['phone2'] = ''
	context['description'] = ''

	if id > 0:
		context['customer'] = Customer.objects.get(id=id)
		context['id'] = context['customer'].id
		context['name'] = context['customer'].name
		context['full_name'] = context['customer'].full_name
		context['inn'] = context['customer'].inn
		context['kpp'] = context['customer'].kpp
		context['email'] = context['customer'].email
		context['address1'] = context['customer'].address1
		context['address2'] = context['customer'].address2
		context['phone1'] = context['customer'].phone1
		context['phone2'] = context['customer'].phone2
		context['description'] = context['customer'].description

	return render(request, "crmapp/customer.html", context)


def new_customer(request):

	return show_customer(request, 0)


def save_customer(request):
	
	id = int(request.POST.get('id', "0"))
	name = request.POST.get('name', '')
	full_name = request.POST.get('fullName', '')
	inn = request.POST.get('inn', '')
	kpp = request.POST.get('kpp', '')
	email = request.POST.get('email', '')
	address1 = request.POST.get('address1', '')
	address2 = request.POST.get('address2', '')
	phone1 = request.POST.get('phone1', '')
	phone2 = request.POST.get('phone2', '')
	description = request.POST.get('description', '')
	
	if id==0:

		if create_new_customer(
			name=name, 
			full_name=full_name, 
			inn=inn, 
			kpp=kpp, 
			email=email,
			address1=address1,
			address2=address2,
			phone1=phone1,
			phone2=phone2,
			description=description):
			return redirect('show-crm-index')
	else:
		if update_customer(Customer.objects.get(id=id),
			name=name, 
			full_name=full_name, 
			inn=inn, 
			kpp=kpp, 
			email=email,
			address1=address1,
			address2=address2,
			phone1=phone1,
			phone2=phone2,
			description=description):
			return redirect('show-crm-index')


	return redirect(request.META['HTTP_REFERER'])


def new_employee(request, customer_id):
	
	context = get_context()
	context['customers'] = Customer.objects.all()
	context['customer'] = Customer.objects.get(id=customer_id)
	context['persons'] = Person.objects.all()
	context['positions'] = Position.objects.all()
	return render(request, "crmapp/employee.html", context)


def show_employee(request, id):
	
	context = get_context()
	context['employee'] = Employee.objects.get(id=id)
	context['customers'] = Customer.objects.all()
	context['customer'] = context['employee'].customer
	context['persons'] = Person.objects.all()
	context['positions'] = Position.objects.all()
	return render(request, "crmapp/employee.html", context)


def save_employee(request):
	
	id = int(request.POST.get('id', "0"))
	name = request.POST.get('name', '')

	customer_id = request.POST.get('customer_id', '')
	person_id = request.POST.get('person_id', '')
	position_id = request.POST.get('position_id', '')
	
	email = request.POST.get('email', '')
	address1 = request.POST.get('address1', '')
	address2 = request.POST.get('address2', '')
	phone1 = request.POST.get('phone1', '')
	phone2 = request.POST.get('phone2', '')
	
	customer = Customer.objects.filter(id=customer_id).first()
	person = Person.objects.filter(id=person_id).first()
	position = Position.objects.filter(id=position_id).first()

	if id==0:

		if create_new_employee(name=name, customer=customer, person=person, position=position, email=email,
			address1=address1, address2=address2, phone1=phone1, phone2=phone2):				
			pass		
	else:
		if update_employee(Employee.objects.get(id=id), name=name, customer=customer, person=person, 
			position=position, email=email, address1=address1, address2=address2, phone1=phone1, phone2=phone2):			
			pass	

	return redirect('show-customer', id=str(customer_id))