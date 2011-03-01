from django.db import models

RELATION_CHOICES = (
	('Father', 'Father'),
	('Mother', 'Mother'),
	('Grand Father', 'Grand Father'),
	('Grand Mother', 'Grand Mother'),
	('Brother', 'Brother'),
	('Sister', 'Sister'),
	('Cousin', 'Cousin'),
	('Child', 'Child'),
	('Step Father', 'Step Father'),
	('Step Mother', 'Step Mother'),
	('Step Brother', 'Step Brother'),
	('Step Sister', 'Step Sister'),
	('Friend', 'Friend'),
	('Acquaintance', 'Acquaintance'),	
)

class Family(models.Model):
	family = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.family
		
class Member(models.Model):
	family = models.ForeignKey('Family')
	contact = models.ForeignKey('contacts.Contact', related_name='member')
	relation = models.CharField(max_length=15, choices=RELATION_CHOICES)
