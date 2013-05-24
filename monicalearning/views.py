
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from news.models import *
from monicalearning.forms import *

def home(request):
	return render(request, 'home.html', {'home' : True})

def our_program(request):
	return render(request, 'our_program.html', { 'program' : True })

def resources(request):
	return render(request, 'resources.html', { 'resources' : True})

def testimony(request):
	return render(request, 'testimony.html')

def news(request):
	return render(request, 'news.html', {'all_news':News_Post.objects.all().order_by('year','month').reverse(), 'all_news_size':len(News_Post.objects.all())})

def admin_news(request):
	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_news = News_Post(title=cd['title'], month=cd['month'], year=cd['year'], news=cd['news'], author=cd['author'])
			new_news.save()
			form = NewsForm()
			if request.user.is_authenticated():
				return render(request, 'admin_news.html', {'logged_in':True, 'added': True,'form':form, 'all_news':News_Post.objects.all().order_by('year','month').reverse()})
			else:
				return render(request, 'admin_news.html', {'added': True,'form':form, 'all_news':News_Post.objects.all().order_by('year','month').reverse()})
	if request.user.is_authenticated():
		form = NewsForm()
		return render(request, 'admin_news.html', {'logged_in':True, 'form':form, 'all_news':News_Post.objects.all().order_by('year','month').reverse()})
	else:
		return render(request, 'admin_news.html', {'all_news':News_Post.objects.all().order_by('year','month').reverse()})
	


def delete(request):
	if request.user.is_authenticated():
		try:
			form = NewsForm()
			item = News_Post.objects.get(id=request.POST.getlist('to_delete')[0])
			item.delete()
		except Exception:
			print "Already Deleted"
		return render(request, 'admin_news.html', {'logged_in':True, 'deleted': True, 'form':form, 'all_news':News_Post.objects.all().order_by('year','month').reverse()})

	else:
		return render(request, 'admin_news.html', {'deleted': True, 'form':form, 'all_news':News_Post.objects.all().order_by('year','month').reverse()})

def login_request(request):
	print(request.POST.values())
	username = request.POST['user']
	password = request.POST['password']

	if(username!="" and password!=""):
		user = authenticate(username=username, password=password)

		if user is not None and user.is_authenticated():
			login(request, user)

	return redirect('admin_news.html')

def logout_request(request):
	logout(request)
	response = redirect('/')
	response.delete_cookie('user_location')
	return response

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