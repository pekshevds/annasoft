from django.shortcuts import render
from django.shortcuts import redirect

from baseapp.core import get_context

from .models import Customer
from .models import CustomerForm

from .models import Employee
from .models import EmployeeForm

from .models import Task
from .models import TaskForm

from .models import Person
from .models import PersonForm

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

from .core import get_current_employee

from .core import get_completed_tasks

from datetime import datetime

# Create your views here.
def show_index(request):
	
	if request.user.is_authenticated:
		context = get_context()	
		return render(request, "crmapp/index.html", context)
	return redirect('show-auth')


def show_kanban(request, onUser=False):
	if request.user.is_authenticated:
		context = get_context()
		if onUser:

			context['tasks_A'] = get_tasks("A", request.user)
			context['tasks_B'] = get_tasks("B", request.user)
			context['tasks_C'] = get_tasks("C", request.user)
		else:
			context['tasks_A'] = get_tasks("A")
			context['tasks_B'] = get_tasks("B")
			context['tasks_C'] = get_tasks("C")
		return render(request, "crmapp/kanban.html", context)
	return redirect('show-auth')


def send_to_B(request, id):

	if request.user.is_authenticated:
		send_task_to_B(id, user=request.user)
	return redirect('show-kanban')


def send_to_C(request, id):

	if request.user.is_authenticated:
		send_task_to_C(id, user=request.user)
	return redirect('show-kanban')


def send_to_D(request, id):

	if request.user.is_authenticated:
		send_task_to_D(id, user=request.user)
	return redirect('show-kanban')


def save_task(request):

	# if request.user.is_authenticated:

	# 	id 					= int(request.POST.get("id", "0"))
	# 	customer_id 		= request.POST.get("customer", "0")
	# 	from_customer_id 	= request.POST.get("from_customer", "0")
	# 	performer_id 		= request.POST.get("performer", "0")
	# 	from_performer_id 	= request.POST.get("from_performer", "0")
		
	# 	try:
	# 		dead_line		= datetime.strptime(request.POST.get("dead_line", None), "%Y-%m-%d")
	# 	except:
	# 		dead_line 		= None

	# 	description 		= request.POST.get("description", "")

	# 	customer 			= Customer.objects.filter(id=customer_id).first()
	# 	from_customer 		= Employee.objects.filter(id=from_customer_id).first()

	# 	performer 			= Customer.objects.filter(id=performer_id).first()
	# 	from_performer 		= Employee.objects.filter(id=from_performer_id).first()


	# 	time_scheduled_h 	= int(request.POST.get("time_scheduled_h", "0"))
	# 	time_scheduled_m 	= int(request.POST.get("time_scheduled_m", "0"))
	# 	time_actual_h 		= int(request.POST.get("time_actual_h", "0"))
	# 	time_actual_m 		= int(request.POST.get("time_actual_m", "0"))
		
	# 	if id == 0:

	# 		if create_new_task(customer=customer, from_customer=from_customer, performer=performer, from_performer=from_performer, 
	# 							dead_line=dead_line, description=description, time_scheduled_h=time_scheduled_h, 
	# 							time_scheduled_m=time_scheduled_m, time_actual_h=time_actual_h, time_actual_m=time_actual_m, user=request.user):
	# 			return redirect('show-kanban')
	# 	else:

	# 		if update_task(task=Task.objects.get(id=id), customer=customer, from_customer=from_customer, performer=performer, 
	# 						from_performer=from_performer, dead_line=dead_line, description=description, time_scheduled_h=time_scheduled_h,
	# 						time_scheduled_m=time_scheduled_m, time_actual_h=time_actual_h, time_actual_m=time_actual_m, user=request.user):
	# 			return redirect('show-kanban')
	if request.user.is_authenticated:
		if request.method == 'POST':
			
			try:
				task = Task.objects.get(id=int(request.POST.get('id', '0')))
			except:
				task = None

			print(task)
			print(request.POST)
			taskForm = TaskForm(request.POST, instance=task)
			if taskForm.is_valid():
				task = taskForm.save(commit=False)

				task.customer = taskForm.cleaned_data['customer']
				task.from_customer = taskForm.cleaned_data['from_customer']
				task.performer = taskForm.cleaned_data['performer']
				task.from_performer = taskForm.cleaned_data['from_performer']

				return redirect('show-kanban')
	return redirect(request.META['HTTP_REFERER'])
	

def show_task(request, id):
	
	task = Task.objects.get(id=id)
	
	context = get_context()	
	context['task']	= TaskForm(instance=task, 
								customer=task.customer,
								performer=task.performer)

	return render(request, "crmapp/task.html", context)


def new_task(request, customer_id):
	
	customer = Customer.objects.get(id=customer_id)

	context = get_context()		
	context['task'] = TaskForm(initial = {
						'customer': customer,
						'performer': get_default_performer(),
					}, 
					customer=customer,
					performer=get_default_performer())

	return render(request, "crmapp/task.html", context)


def show_persons(request):
	if request.user.is_authenticated:
		context 				= get_context()
		context['persons'] 		= Person.objects.all()		
		return render(request, "crmapp/persons.html", context)
	return redirect('show-auth')


def new_person(request):

	context 				= get_context()		
	context['person'] 		= PersonForm()	
	return render(request, "crmapp/person.html", context)


def show_person(request, id):

	if request.user.is_authenticated:

		context 				= get_context()				
		context['person'] 		= PersonForm(instance=Person.objects.get(id=id))		
		return render(request, "crmapp/person.html", context)
	return redirect('show-auth')


def save_person(request):

	if request.user.is_authenticated:
		if request.method == 'POST':
			
			try:
				person = Person.objects.get(id=int(request.POST.get('id', '0')))
			except:
				person = None

			personForm = PersonForm(request.POST, instance=person)
			if personForm.is_valid():
				personForm.save()
				return redirect('persons')

	return redirect(request.META['HTTP_REFERER'])


def show_customers(request):

	if request.user.is_authenticated:
		
		context = get_context()
		context['customers'] = Customer.objects.all()
		return render(request, "crmapp/customers.html", context)
	return redirect('show-auth')


def show_customer(request, id):
	
	if request.user.is_authenticated:
	
		context = get_context()	
		context['customer'] = CustomerForm(instance=Customer.objects.get(id=id))		
		return render(request, "crmapp/customer.html", context)
	return redirect('show-auth')


def new_customer(request):

	context = get_context()	
	context['customer'] = CustomerForm()
	return render(request, "crmapp/customer.html", context)


def save_customer(request):
		
	if request.user.is_authenticated:
		if request.method == 'POST':

			try:
				customer = Customer.objects.get(id=int(request.POST.get('id', '0')))
			except:
				customer = None

			customerForm = CustomerForm(request.POST, instance=customer)
			if customerForm.is_valid():
				customerForm.save()
				return redirect('customers')

	return redirect(request.META['HTTP_REFERER'])


def new_employee(request, customer_id):
	
	if request.user.is_authenticated:
		
		context = get_context()
		context['employee'] = EmployeeForm(initial = {
					'customer': customer_id,					
					})
		return render(request, "crmapp/employee.html", context)
	return redirect('show-auth')


def show_employee(request, id):
	
	if request.user.is_authenticated:
		
		employee = Employee.objects.get(id=id)

		context = get_context()
		context['employee'] = EmployeeForm(instance= employee, 
					initial = {
					'customer': employee.customer.pk,
					'position': employee.position.pk,
					'person': employee.person.pk,
					})

		return render(request, "crmapp/employee.html", context)
	return redirect('show-auth')


def save_employee(request):
		
	if request.user.is_authenticated:
		if request.method == 'POST':

			try:
				employee = Employee.objects.get(id=int(request.POST.get('id', '0')))
			except:
				employee = None

			employeeForm = EmployeeForm(request.POST, instance=employee)
			if employeeForm.is_valid():
				employee = employeeForm.save(commit=False)

				employee.customer = employeeForm.cleaned_data['customer']
				employee.position = employeeForm.cleaned_data['position']
				employee.person = employeeForm.cleaned_data['person']

				employee.save()
				return redirect('show-customer', id=str(employee.customer.pk))

	return redirect(request.META['HTTP_REFERER'])


def show_report_001(request):
	if request.user.is_authenticated:
		context = get_context()

		if request.method == 'POST':

			try:
				param_from		= datetime.strptime(request.POST.get('param_from', datetime.now()), '%Y-%m-%d')
			except:
				param_from		= datetime.now()

			try:
				param_to		= datetime.strptime(request.POST.get('param_to', datetime.now()), '%Y-%m-%d')
			except:
				param_to		= datetime.now()
			
			context['param_from'] = param_from.strftime("%Y-%m-%d")
			context['param_to'] = param_to.strftime("%Y-%m-%d")
			context['tasks'] = get_completed_tasks(param_from=param_from, param_to=param_to)

		return render(request, "crmapp/report_001.html", context)

	return redirect(request.META['HTTP_REFERER'])