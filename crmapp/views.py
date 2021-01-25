from django.shortcuts import render
from django.shortcuts import redirect

from baseapp.core import get_context

from .models import Customer

# Create your views here.
def show_index(request):

	context = get_context()
	context['customers'] = Customer.objects.all()
	return render(request, "crmapp/index.html", context)


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