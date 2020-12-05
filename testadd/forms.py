from django import forms
from .models import address

class addressForm(forms.ModelForm):
	class Meta:
		model = address
		fields = ["name", "address", "city", "state", "zipcode", "received"]