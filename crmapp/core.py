from .models import Task
from .models import Customer
from .models import Person
from .models import Employee


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


def send_task_to_B(id):

	task = Task.objects.get(id=id)
	task.task_status = "B"
	task.save()


def send_task_to_C(id):

	task = Task.objects.get(id=id)
	task.task_status = "C"
	task.save()


def send_task_to_D(id):

	task = Task.objects.get(id=id)
	task.task_status = "D"
	task.save()


def get_default_performer():

	return Customer.objects.filter(is_performer=True).first()


def create_new_task(customer, from_customer, performer, from_performer, dead_line, description,
					time_scheduled_h, time_scheduled_m, time_actual_h, time_actual_m):
	try:
		new_task = Task.objects.create(customer=customer, from_customer=from_customer, performer=performer, from_performer=from_performer,
										dead_line=dead_line, description=description, time_scheduled_h=time_scheduled_h,
										time_scheduled_m=time_scheduled_m, time_actual_h=time_actual_h, time_actual_m=time_actual_m)
	except:
		return False
	return True


def update_task(task, customer, from_customer, performer, from_performer, dead_line, description, 
				time_scheduled_h, time_scheduled_m, time_actual_h, time_actual_m):
	try:
		task.customer = customer 
		task.from_customer = from_customer
		task.performer = performer
		task.from_performer = from_performer
		task.dead_line = dead_line
		task.description = description
		task.time_scheduled_h = time_scheduled_h
		task.time_scheduled_m = time_scheduled_m
		task.time_actual_h = time_actual_h
		task.time_actual_m = time_actual_m
		task.save()
	except:
		return False
	return True


def create_new_customer(name, full_name, inn, kpp, email, address1, address2, phone1, phone2, description):
	try:
		new_customer = Customer.objects.create(name=name, full_name = full_name, inn = inn, kpp = kpp, email = email, 
						address1=address1, address2=address2, phone1=phone1, phone2=phone2, description=description)
	except:
		return False
	return True


def update_customer(customer, name, full_name, inn, kpp, email, address1, address2, phone1, phone2, description):
	try:
		customer.name = name 
		customer.full_name = full_name 
		customer.inn = inn 
		customer.kpp = kpp
		customer.email = email 
		customer.address1 = address1
		customer.address2 = address2
		customer.phone1 = phone1
		customer.phone2 = phone2
		customer.description = description
		customer.save()
	except:
		return False
	return True


def create_new_person(first_name, middle_name, last_name, birthdate, sex, email, address1, address2, phone1, phone2, description):
	try:
		new_task = Person.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name, birthdate=birthdate, 
										sex=sex, email=email, address1=address1, address2=address2, phone1=phone1, phone2=phone2, description=description)
	except:
		return False
	return True


def update_person(person, first_name, middle_name, last_name, birthdate, sex, email, address1, address2, phone1, phone2, description):
	try:
		person.first_name = first_name
		person.middle_name = middle_name
		person.last_name = last_name
		person.birthdate = birthdate
		person.sex = sex
		person.email = email
		person.address1 = address1
		person.address2 = address2
		person.phone1 = phone1
		person.phone2 = phone2
		person.description = description
		person.save()
	except:
		return False
	return True


def create_new_employee(name, customer, person, position, email, address1, address2, phone1, phone2):
	try:
		new_task = Employee.objects.create(name=name, customer=customer, person=person, position=position, email=email,
											address1=address1, address2=address2, phone1=phone1, phone2=phone2)
	except:
		return False
	return True


def update_employee(employee, name, customer, person, position, email, address1, address2, phone1, phone2):
	try:
		employee.name = name
		employee.customer = customer
		employee.person = person
		employee.position = position		
		employee.email = email
		employee.address1 = address1
		employee.address2 = address2
		employee.phone1 = phone1
		employee.phone2 = phone2
		
		employee.save()
	except:
		return False
	return True


def get_employee_on_user(user):
	return Employee.objects.filter(user=user).first()


def get_current_employee(request):
	if request.user.is_authenticated:
		return get_employee_on_user(request.user)
	return None