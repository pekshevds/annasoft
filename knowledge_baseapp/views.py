from django.shortcuts import render
from django.shortcuts import redirect
from .models import Section, Record
from crmapp.models import Customer
from .forms import KnowledgeBaseForm

def show_knowledge_base_props(request):

	if request.user.is_authenticated:

		context = {
			'select_sections': Section.objects.all().order_by('title'),
			'select_customers': Customer.objects.all().order_by('name'),
			'records': Record.objects.all().order_by('customer'),
		}

		return render(request, "knowledge_baseapp/knowledge_base.html", context)

def show_property(request, id):

	if request.user.is_authenticated:

		context = {
			'section': Section.objects.get(id=id),
			'select_sections': Section.objects.all().order_by('title').exclude(id=id),
			'select_customers': Customer.objects.all().order_by('name'),
		}

		return render(request, "knowledge_baseapp/knowledge_base.html", context)

def add_property(request):

	if request.user.is_authenticated:

		if request.method == 'POST':

			section_form = KnowledgeBaseForm(request.POST)

			if section_form.is_valid():

				title = section_form.cleaned_data['input_title']

				section = Section(title=title)

				section.save()

	context = {
		'sections': Section.objects.all().order_by('title'),
		'select_sections': Section.objects.all().order_by('title'),
		'select_customers': Customer.objects.all().order_by('name'),
	}

	return render(request, "knowledge_baseapp/knowledge_base.html", context)

def show_knowledge_base_customers(request):

	if request.user.is_authenticated:

		context = {
			'customers': Customer.objects.all().order_by('name'),
			'select_sections': Section.objects.all().order_by('title'),
			'select_customers': Customer.objects.all().order_by('name'),
		}

		return render(request, "knowledge_baseapp/knowledge_base.html", context)
	
def show_customer(request, id):

	if request.user.is_authenticated:

		customer = Customer.objects.get(id=id)
		section_of_customer = Section.objects.all()

		context = {
			'customer': customer,
			'section_of_customer': section_of_customer,
			'select_sections': Section.objects.all().order_by('title'),
			'select_customers': Customer.objects.all().order_by('name').exclude(id=id),

		}

		return render(request, "knowledge_baseapp/knowledge_base.html", context)

def add_record(request):

	if request.user.is_authenticated:

		if request.method == 'POST':

			record_form = KnowledgeBaseForm(request.POST)

			if record_form.is_valid():

				title = record_form.cleaned_data['input_title']

				if record_form.cleaned_data['input_customer']:

					try:
						customer = Customer.objects.get(id=record_form.cleaned_data['input_customer'])
					except:
						customer = None

				if record_form.cleaned_data['input_section']:
					
					try:
						section = Section.objects.get(id=record_form.cleaned_data['input_section'])
					except:
						section = None		
					
				description = record_form.cleaned_data['input_description']

				new_record = Record(
					title=title,
					customer=customer,
					section=section,
					description=description,	
					)
				new_record.save()

	current_path = request.META['HTTP_REFERER']
	return redirect(current_path)			