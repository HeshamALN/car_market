from django import forms
from django.forms import ModelForm

from .models import Car

class CarForm(forms.ModelForm):
	class Meta:
		model = Car
		fields = '__all__'

# class UpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Car
# 		fields = ['make','model','year','img']


