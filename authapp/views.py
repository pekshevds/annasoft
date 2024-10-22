from django.shortcuts import (
	render,
	redirect
)
from django.contrib.auth import (
	authenticate,
	login,
	logout
)
from django.http import (
	HttpRequest,
	HttpResponse
)
from django.views.generic import View
from django.contrib import messages

from authapp.forms import UserForm

class LoginView(View):

	def get(self, request: HttpRequest) -> HttpResponse:
		return render(request, 'authapp/auth.html')
	
	def post(self, request: HttpRequest) -> HttpResponse:
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			input_username = user_form.cleaned_data.get('username')
			input_password = user_form.cleaned_data.get('password')
			user = authenticate(
				request = request, 
				username = input_username, 
				password = input_password
			)
			if user is not None:
				login(request, user)
				return redirect('show-crm-index')
			else:
				messages.info(request, 'Комбинации пароль-логин не существует!')
				request.session['user_data'] = {
					'username': input_username,
					'password': input_password
				}	
		else:
			messages.info(request, 'Ошибка при вводе данных в форму!')		
		return redirect('authapp:show-auth')	


class LogoutView(View):

	def get(self, request: HttpRequest) -> HttpResponse:
		logout(request)
		return redirect('show-index')