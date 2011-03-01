from contacts.models import Contact, Info
from django.contrib import admin

class InfoInline(admin.TabularInline):
	model = Info

class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['contact']}),
		('Date information', {'fields': ['pub_date'],
			'classes': ['collapse']}),
	]
	inlines = [InfoInline]
	list_display = ('contact', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['contact']
	date_hierarchy = 'pub_date'

admin.site.register(Contact, ContactAdmin)
