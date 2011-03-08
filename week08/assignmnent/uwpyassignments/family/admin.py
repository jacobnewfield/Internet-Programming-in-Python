from family.models import Family, Member
from django.contrib import admin

class MemberInline(admin.TabularInline):
	model = Member
	extra = 1

class FamilyAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['family']}),
		('Date information', {'fields': ['pub_date'],
			'classes': ['collapse']}),
	]
	inlines = [MemberInline]
	list_display = ('family', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['family']
	date_hierarchy = 'pub_date'
	
admin.site.register(Family, FamilyAdmin)
