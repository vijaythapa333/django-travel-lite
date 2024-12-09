from django import forms
from .models import Subscriber



class SubscribeForm(forms.ModelForm):
	class Meta:
		model = Subscriber
		fields = ['subscriber_email',]
		widgets = {
			'subscriber_email': forms.TextInput(attrs={
				'class': 'form-control form-control-lg',
				'placeholder': 'Your Email',
				}),
		}