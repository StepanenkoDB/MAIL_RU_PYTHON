from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError
from django import forms
from .models import Charge
from django.utils import timezone

class ChargeForm(forms.ModelForm):

	class Meta:
		model = Charge
		fields = ('title', 'amount', 'date', 'sign',)

	def clean(self):
		cleaned_data = super(ChargeForm, self).clean()
		value = self.cleaned_data.get('amount')
		if value < 0:
			raise forms.ValidationError({'amount': ["Should be positive: mark outcome by using the checkbox below"]})
		sign = self.cleaned_data.get('sign')
		date = self.cleaned_data.get('date')
		if not sign and date >= timezone.now():
			raise forms.ValidationError({'date': ["Not everyone can watch today to tomorrow :)"]})
		return cleaned_data