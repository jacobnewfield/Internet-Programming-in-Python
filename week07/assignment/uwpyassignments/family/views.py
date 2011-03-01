# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from family.models import Family, Member
from contacts.models import Contact
from django.http import HttpResponse

def index(request):
        latest_family_list = Family.objects.all().order_by('-pub_date')[:5]
        return render_to_response('family/index.html', {'latest_family_list': latest_family_list})

def family(request, family_id):
        f = get_object_or_404(Family, pk=family_id)
        return render_to_response('family/family.html', {'family': f})

def contact(request, contact_id):
	m = get_object_or_404(Contact, pk=contact_id)
	return render_to_response('family/contact.html', {'contact': m})
	#return HttpResponse('Hello World')
