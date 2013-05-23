
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

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
	return render(request, 'contact_us.html')