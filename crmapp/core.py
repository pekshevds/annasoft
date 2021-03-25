from .models import Task
from .models import Customer
from .models import Person
from .models import Employee
from .models import Record


from datetime import datetime
from datetime import timedelta

import pandas as pd


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


def send_task_to_B(id, user):

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


def get_completed_tasks(param_from, param_to, customer=None):
	param_from = datetime(year=param_from.year, month=param_from.month, day=param_from.day,)
	param_to = datetime(year=param_to.year, month=param_to.month, day=param_to.day,)

	if customer:

		return Task.objects.filter(
					customer=customer,
					date_of_completion__gte=param_from.replace(hour=0, minute=0, second=0, microsecond=0), 
					date_of_completion__lte=param_to.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(1)
					)
	else:
	
		return Task.objects.filter(					
					date_of_completion__gte=param_from.replace(hour=0, minute=0, second=0, microsecond=0), 
					date_of_completion__lte=param_to.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(1)
					)




class Record:
	"""docstring for record"""
	def __init__(self, customer, time_scheduled, time_actual):
		self.customer = customer
		self.time_scheduled = time_scheduled
		self.time_actual = time_actual
		self.profit = round(self.time_actual-self.time_scheduled, 1)
		

def get_completed_tasks_on_customers(param_from, param_to, customer=None):
	
	tasks = get_completed_tasks(param_from=param_from, param_to=param_to, customer=customer)

	df = pd.DataFrame.from_records(tasks.values('customer', 'time_scheduled_h', 'time_scheduled_m',
												'time_actual_h', 'time_actual_m'))

	# df = df.groupby(['customer'], as_index=False).agg({
	# 	'time_scheduled_h': 'sum',
	# 	'time_scheduled_m': 'sum',
	# 	'time_actual_h': 'sum',
	# 	'time_actual_m': 'sum',
	# 	})

	records = []

	if tasks:
		df = df.groupby(['customer'], as_index=False)[
			'time_scheduled_h',
			'time_scheduled_m',
			'time_actual_h',
			'time_actual_m',
			].sum()

	
	
		for item in df.itertuples(index=False):
			records.append(Record(Customer.objects.get(id=item.customer),
								item.time_scheduled_h + round(item.time_scheduled_m/60, 1),
								item.time_actual_h + round(item.time_actual_m/60, 1)))
	
	return records
