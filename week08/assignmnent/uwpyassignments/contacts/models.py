from django.db import models
from django.forms import ModelForm

class Contact(models.Model):
	contact = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.contact

class Info(models.Model):
	contact = models.OneToOneField('Contact')
	birthdate = models.DateField('birthdate', blank=True, null=True)
	phone = models.CharField('phone', max_length=15, blank=True)
	cell = models.CharField('cell', max_length=15, blank=True)
	email = models.EmailField('email', max_length=75, blank=True)
	address = models.TextField('address', max_length=200,
		blank=True)
	
class ContactForm(ModelForm):
	class Meta:
		model = Contact

class InfoForm(ModelForm):
	class Meta:
		model = Info


