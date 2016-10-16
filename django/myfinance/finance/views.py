from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Charge

def index(request):
	return render(request, 'finance/index.html', {})

def post_all(request):
	charges = Charge.objects.filter(date__lte=timezone.now()).order_by('date')
	return render(request, 'finance/charges.html', {})