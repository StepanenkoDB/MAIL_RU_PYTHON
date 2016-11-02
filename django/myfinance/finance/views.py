from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Charge
from .forms import ChargeForm
from django.shortcuts import redirect
from datetime import datetime,date
from decimal import Decimal
from random import randint

def index(request):
	return render(request, 'finance/index.html', {})

def post_all(request, info=None):
##### Uncomment all the commented strings in order to use project by its initial goal #####
	#charges = Charge.objects.all()
	rand_charges = list(random_transactions())
	positive_datecharges = filter(lambda x: x[0]>0.0, rand_charges)
	negative_datecharges = [i for i in rand_charges if i not in positive_datecharges]
	#positive_datecharges = filter(lambda x: x.sign, charges)
	#negative_datecharges = [i for i in charges if i not in positive_datecharges]
	return render(request, 'finance/charges.html', {'positive_datecharges': positive_datecharges,'negative_datecharges': negative_datecharges, 'info': info})

def add_charge(request):
	if request.method == "POST":
		form = ChargeForm(request.POST)
		if form.is_valid():
			charge = form.save(commit=False)
			charge.save()
			return redirect('post_all')
	else:
		form = ChargeForm()
		form = ChargeForm(initial={'date': timezone.now()})
	return render(request, 'finance/add_charge.html', {'form': form, })#'info': info})


def random_transactions():
	today = date.today()
	start_date = today.replace(year=2005, month=1, day=1).toordinal()
	end_date = today.toordinal()
	while True:
		start_date = randint(start_date, end_date)
		random_date = date.fromordinal(start_date)
		if random_date >= today:
			break
		random_value = randint(-10000, 10000)
		yield random_value, random_date