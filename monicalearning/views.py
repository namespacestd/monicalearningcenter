
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from news.models import *
from monicalearning.forms import *
from django.core.files import File

deleted = False
uploaded = False
upload_failed = False

def home(request):
	all_news = sortNews(News_Post.objects.all())
	return render(request, 'home.html', {'recent_news1' : all_news[0], 'recent_news2' : all_news[1], 'recent_news3' : all_news[2], 'current_schedule' : Schedule.objects.all()[0].name, 'home' : True})

def our_program(request):
	return render(request, 'our_program.html', {'current_schedule' : Schedule.objects.all()[0].name, 'program' : True })

def resources(request):
	return render(request, 'resources.html', { 'current_schedule' : Schedule.objects.all()[0].name,'resources' : True})

def about_us(request):
	return render(request, 'about_us.html', {'about_us' : True, 'current_schedule' : Schedule.objects.all()[0].name,})

def news(request):
	return render(request, 'news.html', {'current_schedule' : Schedule.objects.all()[0].name,'all_news':sortNews(News_Post.objects.all()), 'all_news_size':len(News_Post.objects.all())})

def admin_news(request):
	global deleted
	delete = deleted
	deleted = False

	global uploaded
	upload = uploaded
	uploaded = False

	global upload_failed
	failed = upload_failed
	upload_failed = False

	if request.method == 'POST':
		form = NewsForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			new_news = News_Post(title=cd['title'], month=cd['month'], year=cd['year'], news=cd['news'], author=cd['author'])
			new_news.save()
			form = NewsForm()
			schedule_form = UploadFileForm()
			if request.user.is_authenticated():
				return render(request, 'admin_news.html', {'uploaded' : upload, 'upload_fail' : failed, 'deleted' : delete,'current_schedule' : Schedule.objects.all()[0].name,'schedule_form':schedule_form, 'logged_in':True, 'added': True,'form':form, 'all_news':sortNews(News_Post.objects.all())})
			else:
				return render(request, 'admin_news.html', {'uploaded' : upload, 'upload_fail' : failed, 'deleted' : delete,'current_schedule' : Schedule.objects.all()[0].name,'schedule_form':schedule_form, 'added': True,'form':form, 'all_news':sortNews(News_Post.objects.all())})
	if request.user.is_authenticated():
		form = NewsForm()
		schedule_form = UploadFileForm()
		return render(request, 'admin_news.html', {'uploaded' : upload, 'upload_fail' : failed,'deleted' : delete, 'current_schedule' : Schedule.objects.all()[0].name,'schedule_form':schedule_form, 'logged_in':True, 'form':form, 'all_news':sortNews(News_Post.objects.all())})
	else:
		return render(request, 'admin_news.html', {'uploaded' : upload, 'upload_fail' : failed,'deleted' : delete, 'current_schedule' : Schedule.objects.all()[0].name,'all_news':sortNews(News_Post.objects.all())})

def sortNews(all_news):
	all_news_list = []
	for news in all_news:
		all_news_list.append(news)

	date_ordering = {
		'January' : 1, 
		'February' : 2,
		'March': 3,
		'April': 4,
		'May': 5,
		'June': 6,
		'July': 7,
		'August': 8,
		'September': 9,
		'October': 10,
		'November': 11,
		'December': 12,
	}
	smallest_index = 0

	for i in range(0, len(all_news_list)):
		smallest_index = i
		for j in range(i+1, len(all_news_list)):
			if all_news_list[j].year > all_news_list[smallest_index].year:
				smallest_index = j
			elif all_news_list[j].year == all_news_list[smallest_index].year:
				if date_ordering[all_news_list[j].month] >= date_ordering[all_news_list[smallest_index].month]:
					smallest_index = j

		temp = all_news_list[i]
		all_news_list[i] = all_news_list[smallest_index]
		all_news_list[smallest_index] = temp

	return all_news_list





def delete(request):
	if request.user.is_authenticated():
		try:
			item = News_Post.objects.get(id=request.POST.getlist('to_delete')[0])
			item.delete()
		except Exception:
			print "Already Deleted"
		global deleted 
		deleted = True
	return redirect('/admin_news')

def upload_schedule(request):
	if request.method == 'POST':
		try:
			handle_uploaded_file(request.FILES['schedule'])
			form = NewsForm()
			schedule_form = UploadFileForm()
			global uploaded
			uploaded = True
		except Exception:
			form = NewsForm()
			schedule_form = UploadFileForm()
			global upload_failed
			upload_failed = True
	return redirect('/admin_news')

def login_request(request):
	username = request.POST['username']
	password = request.POST['password']

	if(username!="" and password!=""):
		user = authenticate(username=username, password=password)

		if user is not None and user.is_authenticated():
			login(request, user)

	return redirect('/admin_news')

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
				
			send_mail("Question Form for: " + cd['name'], info, 'noreply@example.com', ['monicalearning@yahoo.com'], fail_silently=False)
			return render(request, 'contact_us.html', {'contact': True, 'current_schedule' : Schedule.objects.all()[0].name,'email_sent' : True})
	else:
		form = ContactForm()
	return render(request, 'contact_us.html', {'contact': True, 'current_schedule' : Schedule.objects.all()[0].name,'form': form})

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
				
			send_mail("Registration Form for: " + cd['student_name'], info, 'noreply@example.com', ['ihasnamespacestd@gmail.com'], fail_silently=True)
			return render(request, 'register.html', {'current_schedule' : Schedule.objects.all()[0].name,'email_sent' : True})
	else:
		form = RegistrationForm()
	return render(request, 'register.html', {'current_schedule' : Schedule.objects.all()[0].name,'form': form})

def handle_uploaded_file(f):
    with open('monicalearning/static/schedules/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    Schedule.objects.all()[0].delete()
    current_schedule = Schedule(name=f.name)
    current_schedule.save()