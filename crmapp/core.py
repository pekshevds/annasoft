from django.db.models import Sum, Count

from datetime import datetime
from datetime import timedelta

from .models import (
	Task,
	Customer,
	Employee,
	Record
) 


def get_tasks_A():

	return get_tasks("A")


def get_tasks_B():

	return get_tasks("B")


def get_tasks_C():

	return get_tasks("C")


def get_tasks(status="A", user=None):
	if user:
		
		return Task.objects.filter(task_status=status, 
			from_performer=get_employee_on_user(user))
	return Task.objects.filter(task_status=status)


def send_task_to_B(id: str, user):

	task = Task.objects.get(id=id)
	task.task_status = "B"
	task.save()

	add_record(task=task, task_status="B", user=user)


def send_task_to_C(id, user):

	task = Task.objects.get(id=id)
	task.task_status = "C"
	task.save()

	add_record(task=task, task_status="C", user=user)


def send_task_to_D(id, user):

	task = Task.objects.get(id=id)
	task.task_status = "D"
	task.date_of_completion = datetime.now()
	task.save()

	add_record(task=task, task_status="D", user=user)

def send_task_to_E(id, user):

	task = Task.objects.get(id=id)
	task.task_status = "E"
	task.date_of_completion = datetime.now()
	task.save()

	add_record(task=task, task_status="E", user=user)	


def get_default_performer():

	return Customer.objects.filter(is_performer=True).first()


def add_record(task, task_status, user):
	try:
		Record.objects.create(task=task, task_status=task_status, user=user)
	except:
		pass

def get_employee_on_user(user):
	return Employee.objects.filter(user=user).first()


def get_current_employee(request):
	if request.user.is_authenticated:
		return get_employee_on_user(request.user)
	return None


def get_completed_tasks(param_from: datetime.date, param_to: datetime.date, customer: Customer = None):
	param_from = datetime(year=param_from.year, month=param_from.month, day=param_from.day,)
	param_to = datetime(year=param_to.year, month=param_to.month, day=param_to.day,)
	task_list = Task.objects.filter(					
					date_of_completion__gte=param_from.replace(hour=0, minute=0, second=0, microsecond=0), 
					date_of_completion__lte=param_to.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(1),
					task_status = 'D'
				)
	if customer:
		task_list = task_list.filter(customer=customer)
	time_scheduled = round(task_list.aggregate(total_h = Sum("time_scheduled_h", default=0))['total_h'] + \
		task_list.aggregate(total_m = Sum("time_scheduled_m", default=0))['total_m']/60, 1)
	time_actual = round(task_list.aggregate(total_h = Sum("time_actual_h", default=0))['total_h'] + \
		task_list.aggregate(total_m = Sum("time_actual_m", default=0))['total_m']/60, 1)
	return {
		'task_list': task_list,
		'time_scheduled': time_scheduled,
		'time_actual': time_actual
	}


def get_employee_completed_tasks(param_from: datetime.date, param_to: datetime.date, employee: Employee = None):
	param_from = datetime(year=param_from.year, month=param_from.month, day=param_from.day,)
	param_to = datetime(year=param_to.year, month=param_to.month, day=param_to.day,)
	task_list = Task.objects.filter(					
					date_of_completion__gte=param_from.replace(hour=0, minute=0, second=0, microsecond=0), 
					date_of_completion__lte=param_to.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(1),
					task_status = 'D'
				)
	if employee:
		task_list = task_list.filter(from_performer = employee)

	time_scheduled = round(task_list.aggregate(total_h = Sum("time_scheduled_h", default=0))['total_h'] + \
		task_list.aggregate(total_m = Sum("time_scheduled_m", default=0))['total_m']/60, 1)
	time_actual = round(task_list.aggregate(total_h = Sum("time_actual_h", default=0))['total_h'] + \
		task_list.aggregate(total_m = Sum("time_actual_m", default=0))['total_m']/60, 1)
	
	return {
		'task_list': task_list,
		'time_scheduled': time_scheduled,
		'time_actual': time_actual
	}


def group_task_by_customer(tasks):
	customer_list = (tasks
		.values('customer')
		.annotate(item_count=Count('customer'))
		.order_by()
	)
	grouped_tasks = []
	for customer_id in customer_list:
		customer = Customer.objects.get(id=customer_id.get('customer'))
		time_actual_amount = round(tasks.filter(customer=customer).aggregate(total_h = Sum("time_actual_h", default=0))['total_h'] + \
				tasks.filter(customer=customer).aggregate(total_m = Sum("time_actual_m", default=0))['total_m']/60, 1)
		time_scheduled_amount = round(tasks.filter(customer=customer).aggregate(total_h = Sum("time_scheduled_h", default=0))['total_h'] + \
				tasks.filter(customer=customer).aggregate(total_m = Sum("time_scheduled_m", default=0))['total_m']/60, 1)
		profit = time_actual_amount - time_scheduled_amount
		grouped_tasks.append({
				'customer': customer.name,
				'tasks': tasks.filter(customer=customer),
				'time_actual_amount': time_actual_amount,
				'time_scheduled_amount': time_scheduled_amount,
				'profit': round(profit, 1)
			})
	return grouped_tasks


def group_task_by_employee(tasks):
	employee_list = (tasks
		.values('from_performer')
		.annotate(item_count=Count('from_performer'))
		.order_by()
	)
	grouped_tasks = []
	for employee_id in employee_list:
		employee = Employee.objects.get(id=employee_id.get('from_performer'))
		time_actual_amount = round(tasks.filter(from_performer=employee).aggregate(total_h = Sum("time_actual_h", default=0))['total_h'] + \
					tasks.filter(from_performer=employee).aggregate(total_m = Sum("time_actual_m", default=0))['total_m']/60, 1)
		time_scheduled_amount = round(tasks.filter(from_performer=employee).aggregate(total_h = Sum("time_scheduled_h", default=0))['total_h'] + \
					tasks.filter(from_performer=employee).aggregate(total_m = Sum("time_scheduled_m", default=0))['total_m']/60, 1)
		profit = time_actual_amount - time_scheduled_amount
		grouped_tasks.append({
				'employee': employee.get_fio_person,
				'tasks': tasks.filter(from_performer=employee),
				'time_actual_amount': time_actual_amount,
				'time_scheduled_amount': time_scheduled_amount,
				'profit': profit
			})
	return grouped_tasks