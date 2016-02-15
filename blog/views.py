from django.shortcuts import render
from django.utils import timezone
from .models import Session
from .models import Beacon
from .models import Speaker
from django.core import serializers

# Create your views here.
def session_list(request):    
	data = serializers.serialize("json", Session.objects.all())
	return render(request, 'blog/session_list.html', {'data': Session.objects.all()})

def beacon_list(request):    
	data = serializers.serialize("json", Beacon.objects.all())
	return render(request, 'blog/beacon_list.html', {'data': Beacon.objects.all()})


