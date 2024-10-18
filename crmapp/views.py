from django.shortcuts import (
	render,
	redirect,
	get_object_or_404
)
from django.views.generic import View
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import date

from crmapp.models import (
	Customer,
	Employee,
	Task,
	Person
)
from crmapp.forms import (
	CustomerForm,
	EmployeeForm,
	TaskForm,
	PersonForm,
	report_001_Form,
	report_002_Form,
	report_003_Form
)
from crmapp.core import (
	get_tasks,
	send_task_to_B,
	send_task_to_C,
	send_task_to_D,
	send_task_to_E,
	get_completed_tasks,
	get_employee_completed_tasks,
	group_task_by_customer,
	group_task_by_employee,
)
from knowledge_baseapp.models import (
	Record,
	Customer,
	Section
)


class CRMIndexView(LoginRequiredMixin, View):
	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, 'crmapp/index.html')


class KanbanView(LoginRequiredMixin, View):
	def get(self, request: HttpRequest, onUser: bool = False) -> HttpResponse:
		if onUser:
			context = {
				'tasks_A': get_tasks("A", request.user),
				'tasks_B': get_tasks("B", request.user),
				'tasks_C': get_tasks("C", request.user)
			}
		else:
			context = {
				'tasks_A': get_tasks("A"),
				'tasks_B': get_tasks("B"),
				'tasks_C': get_tasks("C")
			}
		context['onUser'] = onUser
		return render(request, 'crmapp/kanban.html', context)


class SendToBView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id:str) -> HttpResponse:
		send_task_to_B(id, user=request.user)
		return redirect(request.META['HTTP_REFERER'])


class SendToCView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id:str) -> HttpResponse:
		send_task_to_C(id, user=request.user)
		return redirect(request.META['HTTP_REFERER'])


class SendToDView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id:str) -> HttpResponse:
		send_task_to_D(id, user=request.user)
		return redirect(request.META['HTTP_REFERER'])


class SendToEView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id:str) -> HttpResponse:
		send_task_to_E(id, user=request.user)
		return redirect('show-kanban')


class SaveTaskView(LoginRequiredMixin, View):

	def post(self, request: HttpRequest) -> HttpResponse:
		taskForm = TaskForm(request.POST)			
		if taskForm.is_valid():
			try:
				task = Task.objects.get(id=taskForm.cleaned_data.get('id'))
			except:
				task = Task()
			task.customer = Customer.objects.filter(id=taskForm.cleaned_data['customer']).first()
			task.from_customer = taskForm.cleaned_data['from_customer']
			task.performer = Customer.objects.filter(id=taskForm.cleaned_data['performer']).first()
			task.from_performer = taskForm.cleaned_data['from_performer']
			task.dead_line = taskForm.cleaned_data['dead_line']
			task.description = taskForm.cleaned_data['description']
			task.time_scheduled_h = taskForm.cleaned_data['time_scheduled_h']
			task.time_scheduled_m = taskForm.cleaned_data['time_scheduled_m']
			task.time_actual_h = taskForm.cleaned_data['time_actual_h']
			task.time_actual_m = taskForm.cleaned_data['time_actual_m']
			task.for_payment = taskForm.cleaned_data['for_payment']
			task.save()	

			return redirect('show-task', id=task.id)
			

class TaskView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id: str) -> HttpResponse:
		task = get_object_or_404(Task, id = id)
		context = {
			'task': TaskForm(initial = {
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
				'for_payment': task.for_payment,
			}),
			'customer': task.customer,
			'caption': task,
			'is_ready': task.is_ready()
		}
		return render(request, "crmapp/task.html", context)


class NewTaskView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, customer_id: str) -> HttpResponse:
		
		customer = get_object_or_404(Customer, id=customer_id)
		performer = Customer.objects.filter(is_performer=True).first()
		context = {
			'task': TaskForm (
						initial = {
								'customer': customer.id,
								'customer_name': customer.name,
								'performer': performer.id,
								'performer_name': performer.name,
								'dead_line': date.today(),
							}, 
						customer=customer,
						performer=performer
					),
			'customer': customer,
			'caption': 'Новая задача',
			'is_ready': False
		}
		return render(request, "crmapp/new_task.html", context)


class PersonListView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			'persons': Person.objects.all()
		}
		return render(request, "crmapp/persons.html", context)

class NewPersonView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			'person': PersonForm()
		}
		return render(request, "crmapp/person.html", context)


class PersonView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id: str) -> HttpResponse:
		person = get_object_or_404(Person, id = id)
		context = {
			'person': PersonForm(instance=person)
		}
		return render(request, "crmapp/person.html", context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		personForm = PersonForm(request.POST)
		if personForm.is_valid():
			try:
				person = Person.objects.get(id=personForm.cleaned_data.get('id'))
			except:
				person = None	
			personForm = PersonForm(request.POST, instance=person)
			personForm.save()
			return redirect('persons')


class CustomerListView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		context ={
			'customers': Customer.objects.all()
		}
		return render(request, "crmapp/customers.html", context)


class CustomerView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id: str) -> HttpResponse:
		customer = get_object_or_404(Customer, id = id)
		context = {
			'customer': CustomerForm(instance = customer),
			'info': Record.objects.filter(customer__id=id).order_by('-id')[:3],
			'select_sections': Section.objects.all().order_by('title')
		}
		return render(request, "crmapp/customer.html", context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		customerForm = CustomerForm(request.POST)
		if customerForm.is_valid():
			try:
				customer = Customer.objects.get(id=customerForm.cleaned_data.get('id'))
			except:
				customer = None	
			customerForm = CustomerForm(request.POST, instance=customer)
			customerForm.save()
			return redirect('customers')


class NewCustomerView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		context = {
			'customer': CustomerForm()
		}
		return render(request, "crmapp/new_customer.html", context)


class EmployeeView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, id: str) -> HttpResponse:
		employee = get_object_or_404(Employee, id = id)
		context = {
			'employee': EmployeeForm(
				instance = employee,
				initial = {
					'customer': employee.customer.pk,
					'position': employee.position.pk,
					'person': employee.person.pk,
				})
		}
		return render(request, "crmapp/employee.html", context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		employeeForm = EmployeeForm(request.POST)
		if employeeForm.is_valid():
			try:
				employee = Employee.objects.get(pk=employeeForm.cleaned_data.get('id'))
			except:
				employee = None
			employeeForm = EmployeeForm(request.POST, instance=employee)
			employee = employeeForm.save(commit=False)
			employee.customer = employeeForm.cleaned_data['customer']
			employee.position = employeeForm.cleaned_data['position']
			employee.person = employeeForm.cleaned_data['person']
			employee.save()
			return redirect('show-customer', id=employee.customer.pk)


class NewEmployeeView(LoginRequiredMixin, View):

	def get(self, request: HttpRequest, customer_id: str) -> HttpResponse:
		context = {
			'employee': EmployeeForm(initial = {
				'customer': customer_id
			})
		}
		return render(request, 'crmapp/employee.html', context)


# Закрытые задачи
class ReportListView(LoginRequiredMixin, View):
	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, 'crmapp/reports.html')


class Report001View(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		param_from = param_to = date.today()
		customer = None				
		tasks_info = get_completed_tasks(
			param_from=param_from, 
			param_to=param_to
		)
		reportForm = report_001_Form(
			initial={
				'param_from': param_from,
				'param_to': param_to,
				'customer': customer,					
			})
		context = {
			'settings': reportForm,
			'tasks': tasks_info.get('task_list'),
			'time_scheduled': tasks_info.get('time_scheduled'),
			'time_actual': tasks_info.get('time_actual'),
			'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
		}
		return render(request, 'crmapp/report_001.html', context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		report_form = report_001_Form(request.POST)
		if report_form.is_valid():
			param_from = report_form.cleaned_data['param_from']
			param_to = report_form.cleaned_data['param_to']
			customer = report_form.cleaned_data['customer']
			tasks_info = get_completed_tasks(
				param_from=param_from, 
				param_to=param_to,
				customer=customer
			)
			reportForm = report_001_Form(
				initial = {
					'param_from': param_from,
					'param_to': param_to,
					'customer': customer,					
			})
			context = {
				'settings': reportForm,
				'tasks': tasks_info.get('task_list'),
				'time_scheduled': tasks_info.get('time_scheduled'),
				'time_actual': tasks_info.get('time_actual'),
				'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
			}
			return render(request, 'crmapp/report_001.html', context)


#Выработка по заказчикам
class Report002View(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		param_from = param_to = date.today()
		customer = None				
		tasks_info = get_completed_tasks(
			param_from=param_from, 
			param_to=param_to
		)
		reportForm = report_002_Form(
			initial={
				'param_from': param_from,
				'param_to': param_to,
				'customer': customer,					
			})
		context = {
			'settings': reportForm,
			'grouped_tasks': group_task_by_customer(tasks_info.get('task_list')),
			'time_scheduled': tasks_info.get('time_scheduled'),
			'time_actual': tasks_info.get('time_actual'),
			'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
		}
		return render(request, 'crmapp/report_002.html', context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		report_form = report_002_Form(request.POST)
		if report_form.is_valid():
			param_from = report_form.cleaned_data['param_from']
			param_to = report_form.cleaned_data['param_to']
			customer = report_form.cleaned_data['customer']
			tasks_info = get_completed_tasks(
				param_from=param_from, 
				param_to=param_to,
				customer=customer
			)
			reportForm = report_002_Form(
				initial = {
					'param_from': param_from,
					'param_to': param_to,
					'customer': customer,					
			})
			context = {
				'settings': reportForm,
				'grouped_tasks': group_task_by_customer(tasks_info.get('task_list')),
				'time_scheduled': tasks_info.get('time_scheduled'),
				'time_actual': tasks_info.get('time_actual'),
				'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
			}
			return render(request, 'crmapp/report_002.html', context)


#Выработка по исполнителям
class Report003View(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		param_from = param_to = date.today()
		employee = None				
		tasks_info = get_employee_completed_tasks(
			param_from=param_from, 
			param_to=param_to
		)
		reportForm = report_003_Form(
			initial={
				'param_from': param_from,
				'param_to': param_to,
				'employee': employee,					
			})
		context = {
			'settings': reportForm,
			'grouped_tasks': group_task_by_employee(tasks_info.get('task_list')),
			'time_scheduled': tasks_info.get('time_scheduled'),
			'time_actual': tasks_info.get('time_actual'),
			'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
		}
		return render(request, 'crmapp/report_003.html', context)

	def post(self, request: HttpRequest) -> HttpResponse:
		report_form = report_003_Form(request.POST)
		if report_form.is_valid():
			param_from = report_form.cleaned_data['param_from']
			param_to = report_form.cleaned_data['param_to']
			employee = report_form.cleaned_data['employee']
			tasks_info = get_employee_completed_tasks(
				param_from=param_from, 
				param_to=param_to,
				employee=employee
			)
			reportForm = report_003_Form(
				initial = {
					'param_from': param_from,
					'param_to': param_to,
					'employee': employee,					
			})
			context = {
				'settings': reportForm,
				'grouped_tasks': group_task_by_employee(tasks_info.get('task_list')),
				'time_scheduled': tasks_info.get('time_scheduled'),
				'time_actual': tasks_info.get('time_actual'),
				'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
			}
			return render(request, 'crmapp/report_003.html', context)


class Report004View(LoginRequiredMixin, View):
	
	def get(self, request: HttpRequest) -> HttpResponse:
		param_from = param_to = date.today()
		customer = None				
		tasks_info = get_completed_tasks(
			param_from=param_from, 
			param_to=param_to
		)
		reportForm = report_001_Form(
			initial={
				'param_from': param_from,
				'param_to': param_to,
				'customer': customer,					
			})
		context = {
			'settings': reportForm,
			'grouped_tasks': group_task_by_customer(tasks_info.get('task_list')),
			'time_scheduled': tasks_info.get('time_scheduled'),
		}
		return render(request, 'crmapp/report_004.html', context)
	
	def post(self, request: HttpRequest) -> HttpResponse:
		report_form = report_001_Form(request.POST)
		if report_form.is_valid():
			param_from = report_form.cleaned_data['param_from']
			param_to = report_form.cleaned_data['param_to']
			customer = report_form.cleaned_data['customer']
			tasks_info = get_completed_tasks(
				param_from=param_from, 
				param_to=param_to,
				customer=customer
			)
			reportForm = report_001_Form(
				initial = {
					'param_from': param_from,
					'param_to': param_to,
					'customer': customer,					
			})
			context = {
				'settings': reportForm,
				'grouped_tasks': group_task_by_customer(tasks_info.get('task_list')),
				'time_scheduled': tasks_info.get('time_scheduled'),
			}
			return render(request, 'crmapp/report_004.html', context)


#Выработка по исполнителям
class Report005View(LoginRequiredMixin, View):

	def get(self, request: HttpRequest) -> HttpResponse:
		param_from = param_to = date.today()
		employee = None				
		tasks_info = get_employee_completed_tasks(
			param_from=param_from, 
			param_to=param_to
		)
		reportForm = report_003_Form(
			initial={
				'param_from': param_from,
				'param_to': param_to,
				'employee': employee,					
			})
		context = {
			'settings': reportForm,
			'grouped_tasks': group_task_by_employee(tasks_info.get('task_list')),
			'time_scheduled': tasks_info.get('time_scheduled'),
			'time_actual': tasks_info.get('time_actual'),
			'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
		}
		return render(request, 'crmapp/report_005.html', context)

	def post(self, request: HttpRequest) -> HttpResponse:
		report_form = report_003_Form(request.POST)
		if report_form.is_valid():
			param_from = report_form.cleaned_data['param_from']
			param_to = report_form.cleaned_data['param_to']
			employee = report_form.cleaned_data['employee']
			tasks_info = get_employee_completed_tasks(
				param_from=param_from, 
				param_to=param_to,
				employee=employee
			)
			reportForm = report_003_Form(
				initial = {
					'param_from': param_from,
					'param_to': param_to,
					'employee': employee,					
			})
			context = {
				'settings': reportForm,
				'grouped_tasks': group_task_by_employee(tasks_info.get('task_list')),
				'time_scheduled': tasks_info.get('time_scheduled'),
				'time_actual': tasks_info.get('time_actual'),
				'profit': round(tasks_info.get('time_actual') - tasks_info.get('time_scheduled'), 1)
			}
			return render(request, 'crmapp/report_005.html', context)