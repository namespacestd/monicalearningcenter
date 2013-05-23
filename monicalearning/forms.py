from django import forms

class RegistrationForm(forms.Form):
	student_name = forms.CharField()
	email = forms.EmailField(required=False)
	other_comments = forms.CharField(widget=forms.Textarea)

