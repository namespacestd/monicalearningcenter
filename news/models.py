from django.db import models
from django import forms

class Schedule(models.Model):
	name = models.CharField(max_length=50)

class News_Post(models.Model):
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
	title = models.CharField(max_length=30)
	month = models.CharField(max_length=15, choices=NEWS_MONTHS, default='January')
	year = models.IntegerField(max_length=4)
	news = models.TextField()
	author = models.CharField(max_length=30, blank=True)

	def __unicode__(self):
		return self.title
