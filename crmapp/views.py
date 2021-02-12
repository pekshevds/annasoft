from django.shortcuts import render
from django.shortcuts import redirect

from baseapp.core import get_context

from .models import Customer
from .models import Employee

from .core import get_tasks
from .core import send_task_to_B
from .core import send_task_to_C
from .core import get_default_performer
from .core import create_new_task

from datetime import datetime

# Create your views here.
def show_index(request):

	context = get_context()
	context['customers'] = Customer.objects.all()
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


def save_task(request):

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

	create_new_task(customer=customer, 
		from_customer=from_performer, 
		performer=performer, 
		from_performer=from_performer, 
		dead_line=dead_line, 
		description=description)

	return redirect('show-canban')


def show_task(request, id):
	
	return redirect('show-canban')


def new_task(request, customer_id):
	
	context = get_context()	
	context['customer'] = Customer.objects.get(id=customer_id)
	context['performer'] = get_default_performer()

	return render(request, "crmapp/task.html", context)


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


def save_customer(request):
	
	return redirect(request.META['HTTP_REFERER'])