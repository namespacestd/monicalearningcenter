
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from monicalearning.forms import *

def home(request):
	return render(request, 'home.html', {'home' : True})

def our_program(request):
	return render(request, 'our_program.html', { 'program' : True })

def resources(request):
	return render(request, 'resources.html', { 'resources' : True})

def testimony(request):
	return render(request, 'testimony.html')

def register(request):
	return render(request, 'register.html')

def contact_us(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(cd['student_name'], cd['email'], cd['other_comments'], cd.get('email', 'noreply@example.com'), ['ihasnamespacestd@gmail.com'],)
			return render(request, 'contact_us.html')
	else:
		form = RegistrationForm()
	return render(request, 'contact_us.html', {'form': form})