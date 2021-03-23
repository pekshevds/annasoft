from .models import Task
from .models import Customer
from .models import Person
from .models import Employee
from .models import Record


from datetime import datetime
from datetime import timedelta

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


def get_completed_tasks(param_from, param_to):

	return Task.objects.filter(date_of_completion__gte=param_from.replace(hour=0, minute=0, second=0, microsecond=0), 
		date_of_completion__lte=param_to.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(1))