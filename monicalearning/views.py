
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

def contact_us(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			info = ""
			for field in form:
				try:
					info += (field.label + ": " + cd[field.html_name] + "\n")
				except Exception: 
					info += (field.label + ": " + "<Not Filled In>" + "\n")
				
			send_mail("Question Form for: " + cd['name'], info, 'noreply@example.com', ['ihasnamespacestd@gmail.com'], fail_silently=False)
			return render(request, 'contact_us.html', {'email_sent' : True})
	else:
		form = ContactForm()
	return render(request, 'contact_us.html', {'form': form})

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			info = ""
			for field in form:
				try:
					info += (field.label + ": " + cd[field.html_name] + "\n")
				except Exception: 
					info += (field.label + ": " + "<Not Filled In>" + "\n")
				
			send_mail("Registration Form for: " + cd['student_name'], info, 'noreply@example.com', ['ihasnamespacestd@gmail.com'], fail_silently=False)
			return render(request, 'register.html', {'email_sent' : True})
	else:
		form = RegistrationForm()
	return render(request, 'register.html', {'form': form})