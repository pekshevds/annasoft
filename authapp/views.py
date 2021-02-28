from django.shortcuts import render
from django.shortcuts import redirect

from baseapp.core import get_context

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import UserForm

# Create your views here.
def show_auth(request):

	context = get_context()
	return render(request, "authapp/auth.html", context)


def set_login(request):

	if request.method == 'POST':
		userForm = UserForm(request.POST)

		if userForm.is_valid():
			
			username = userForm.cleaned_data['username']
			password = userForm.cleaned_data['password']
			
			user = authenticate(request, username=username, password=password)			
			if user is not None:
				login(request, user)
				return redirect('show-crm-index')
	return redirect(request.META['HTTP_REFERER'])



def set_logout(request):

	if request.user.is_authenticated:
		logout(request)
	return redirect('show-index')