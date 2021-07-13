from django import forms
 
class KnowledgeBaseForm(forms.Form):

	input_title  		= forms.CharField(max_length = 100)
	input_customer  	= forms.CharField(max_length = 50, required=False)
	input_section  		= forms.CharField(max_length = 50, required=False)
	input_description  	= forms.CharField(max_length = 2048, required=False)