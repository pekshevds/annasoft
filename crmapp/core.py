from .models import Task
from .models import Customer


def get_tasks_A():

	return get_tasks("A")


def get_tasks_B():

	return get_tasks("B")


def get_tasks_C():

	return get_tasks("C")


def get_tasks(status="A"):

	return Task.objects.filter(task_status=status)


def send_task_to_B(id):

	task = Task.objects.get(id=id)
	task.task_status = "B"
	task.save()


def send_task_to_C(id):

	task = Task.objects.get(id=id)
	task.task_status = "C"
	task.save()


def get_default_performer():

	return Customer.objects.filter(is_performer=True).first()


def create_new_task(customer, from_customer, performer, from_performer, dead_line, description):
	try:
		new_task = Task.objects.create(customer=customer, 
										from_customer=from_customer, 
										performer=performer, 
										from_performer=from_performer,
										dead_line=dead_line, 
										description=description)
	except:
		return False
	return True