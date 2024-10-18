from django.shortcuts import (
    render,
    redirect,
	get_object_or_404
)
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from knowledge_baseapp.models import (
	Section, 
    Record
)    
from knowledge_baseapp.forms import KnowledgeBaseRecordForm
from crmapp.models import Customer


class AddRecordView(LoginRequiredMixin, View):
	def post(self, request: HttpRequest) -> HttpResponse:
		record_form  = KnowledgeBaseRecordForm(request.POST)
		if record_form.is_valid():
			Record.objects.create(
				title = record_form.cleaned_data.get('input_title'),
				customer = Customer.objects.filter(id=record_form.cleaned_data.get('input_customer')).first(),
				section = Section.objects.filter(id=record_form.cleaned_data.get('input_section')).first(),
				description = record_form.cleaned_data.get('input_description'),
			)
		return redirect(request.META['HTTP_REFERER'])


class SaveRecordView(LoginRequiredMixin, View):
	def post(self, request: HttpRequest, id: str) -> HttpResponse:
		record_form = KnowledgeBaseRecordForm(request.POST)
		if record_form.is_valid():
			record = get_object_or_404(Record, id=id)
			record.title = record_form.cleaned_data.get('input_title')
			record.description = record_form.cleaned_data.get('input_description')
			record.customer = Customer.objects.filter(id=record_form.cleaned_data.get('input_customer')).first()
			record.section = Section.objects.filter(id=record_form.cleaned_data.get('input_section')).first()
			record.save()
		return redirect(request.META['HTTP_REFERER'])	


class RecordView(LoginRequiredMixin, View):
	def get(self, request: HttpRequest, id: str) -> HttpResponse:
		if request.user.is_authenticated:
			record = get_object_or_404(Record, id=id)
			context = {
				'record': record,
				'select_sections': Section.objects.all().order_by('title').exclude(id=record.section.id)
			}
			return render(request, "knowledge_baseapp/record.html", context)


class RecordsListView(LoginRequiredMixin, View):
	def get(self, request: HttpRequest) -> HttpResponse:
		customer = get_object_or_404(Customer, id=request.GET.get('customer_id'))
		context ={
			'records': Record.objects.filter(customer__id=customer.id),
			'customer': customer,
			'select_sections': Section.objects.all().order_by('title')
		}
		return render(request, 'knowledge_baseapp/records.html', context)