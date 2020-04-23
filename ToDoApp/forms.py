from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from ToDoApp.models import main
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class mainform(forms.ModelForm):
	class Meta:
		model = main
		fields = '__all__'