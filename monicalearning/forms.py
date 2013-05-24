from django import forms

class RegistrationForm(forms.Form):
	PROGRAMS = (
		{'-', '<None Selected>'},
		('Full Day', 'Full Day'),
		('Half Day', 'Half Day'),
		('SAT', 'SAT'),
	)
	LOCATIONS = (
		{'-', '<None Selected>'},
		('Mission (SF)', 'Mission (SF)'),
		('Sunset (SF)', 'Sunset (SF)')
	)
	HEAR = (
		{'-', '<None Selected>'},
		('Television', 'Television'),
		('Newspaper', 'Newspaper'),
		('Radio', 'Radio'),
		('Friend', 'Friend'),
		('Other', 'Other')
	)
	student_name = forms.CharField(label="Student Name")
	email = forms.EmailField(required=False)
	phone = forms.CharField(max_length=15)
	address = forms.CharField(max_length=30)
	city = forms.CharField(max_length=30)
	grade = forms.CharField(max_length=10)
	parent_1_name = forms.CharField(label="Parent 1 Name", max_length=30)
	parent_1_phone = forms.CharField(label = "Parent 1 Phone", max_length=15)
	parent_2_name = forms.CharField(required=False, label="Parent 2 Name", max_length=30)
	parent_2_phone = forms.CharField(required = False, label = "Parent 2 Phone", max_length=15)
	program_selection = forms.ChoiceField(label="Program Selection", choices=PROGRAMS)
	program_duration = forms.CharField(required=False, label="Program Duration", max_length=20)
	location = forms.ChoiceField(required = False, choices = LOCATIONS)
	best_time = forms.CharField(required=False, label = "When would be the best time to call?", max_length=30)
	hear = forms.ChoiceField(required=False, label = "How did you hear about MLC?", choices = HEAR)
	other = forms.CharField(required=False, label = "If other, please specify")
	other_comments = forms.CharField(required=False, widget=forms.Textarea)

class ContactForm(forms.Form):
	LOCATIONS = (
		{'-', '<None Selected>'},
		('Mission (SF)', 'Mission (SF)'),
		('Sunset (SF)', 'Sunset (SF)')
	)
	name = forms.CharField(max_length=30)
	phone = forms.CharField(max_length=15)
	email = forms.EmailField(max_length=30)
	location = forms.ChoiceField(label = "Pick-Up Location", required = False, choices = LOCATIONS)
	questions = forms.CharField(widget=forms.Textarea)

	
class NewsForm(forms.Form):
	NEWS_MONTHS = (
		('January', 'A-January'),
		('February', 'B-February'),
		('March', 'C-March'),
		('April', 'D-April'),
		('May', 'E-May'),
		('June', 'F-June'),
		('July', 'G-July'),
		('August', 'H-August'),
		('September', 'I-September'),
		('October', 'J-October'),
		('November', 'K-November'),
		('December', 'L-December'),
	)
	title = forms.CharField(max_length=30, required = False)
	month = forms.ChoiceField(choices=NEWS_MONTHS)
	year = forms.IntegerField()
	news = forms.CharField(widget=forms.Textarea)
	author = forms.CharField(max_length=30, required = False)

class UploadFileForm(forms.Form):
	schedule  = forms.FileField()



