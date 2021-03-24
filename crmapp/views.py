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

from .forms import show_report_001_Form

from .core import get_tasks
from .core import send_task_to_B
from .core import send_task_to_C
from .core import send_task_to_D
from .core import get_default_performer

from .core import get_current_employee

from .core import get_completed_tasks

from datetime import datetime
from datetime import date

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

	
	if request.user.is_authenticated:
		if request.method == 'POST':
			
			try:
				task = Task.objects.get(id=int(request.POST.get('id', '0')))
			except:
				task = None

			taskForm = TaskForm(request.POST)			
			if taskForm.is_valid():
				
				if not task:
					task = Task()

				task.customer = Customer.objects.get(id=int(taskForm.cleaned_data['customer']))
				task.from_customer = taskForm.cleaned_data['from_customer']
				task.performer = Customer.objects.get(id=int(taskForm.cleaned_data['performer']))
				task.from_performer = taskForm.cleaned_data['from_performer']

				task.dead_line = taskForm.cleaned_data['dead_line']
				task.description = taskForm.cleaned_data['description']
				task.time_scheduled_h = taskForm.cleaned_data['time_scheduled_h']
				task.time_scheduled_m = taskForm.cleaned_data['time_scheduled_m']
				task.time_actual_h = taskForm.cleaned_data['time_actual_h']
				task.time_actual_m = taskForm.cleaned_data['time_actual_m']

				task.save()

				return redirect('show-kanban')
			
	return redirect(request.META['HTTP_REFERER'])
	

def show_task(request, id):
	
	task = Task.objects.get(id=id)
	
	context = get_context()	
	context['task']	= TaskForm(initial = {
						'id': task.id,
						'customer': task.customer.id,
						'customer_name': task.customer.name,
						'from_customer': task.from_customer,

						'performer': task.performer.id,
						'performer_name': task.performer.name,						
						'from_performer': task.from_performer,
						
						'dead_line': task.dead_line,
						
						'time_scheduled_h': task.time_scheduled_h,
						'time_scheduled_m': task.time_scheduled_m,
						'time_actual_h': task.time_actual_h,
						'time_actual_m': task.time_actual_m,
						
						'description': task.description,
					}, 
								customer=task.customer,
								performer=task.performer)
	context['customer']	= task.customer
	context['caption']	= task
	return render(request, "crmapp/task.html", context)


def new_task(request, customer_id):
	
	customer = Customer.objects.get(id=customer_id)
	performer = get_default_performer()

	context = get_context()		
	context['task'] = TaskForm(initial = {
						'customer': customer.id,
						'customer_name': customer.name,
						'performer': performer.id,
						'performer_name': performer.name,
						'dead_line': date.today(),
					}, 
					customer=customer,
					performer=performer)	
	context['customer']	= customer
	context['caption']	= 'Новая задача'
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

		param_from		= date.today()
		param_to		= date.today()
		customer 		= None				
		tasks 			= None

		
		if request.method == 'POST':
			
			reportForm = show_report_001_Form(request.POST)
			if reportForm.is_valid():
				
				param_from = reportForm.cleaned_data['param_from']
				param_to = reportForm.cleaned_data['param_to']
				customer = reportForm.cleaned_data['customer']

				tasks = get_completed_tasks(
					param_from=param_from, 
					param_to=param_to, 
					customer=customer)
			
		reportForm = show_report_001_Form(initial={
					'param_from': param_from,
					'param_to': param_to,
					'customer': customer,
					'tasks': tasks,
					})

		time_scheduled_m = 0
		time_actual_m = 0

		for task in tasks:
			try:
				time_scheduled_m = time_scheduled_m + task.time_scheduled_m
			except:
				time_scheduled_m = time_scheduled_m + 0

			try:
				time_actual_m = time_actual_m + task.time_actual_m
			except:
				time_actual_m = time_actual_m + 0

		context['settings'] = reportForm
		context['time_scheduled_m'] = time_scheduled_m
		context['time_actual_m'] = time_actual_m
		context['profit'] = time_scheduled_m - time_actual_m
		return render(request, "crmapp/report_001.html", context)

	return redirect(request.META['HTTP_REFERER'])