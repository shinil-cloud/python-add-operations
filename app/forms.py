from django import forms
from app.models import Ert



class ErtForm(forms.ModelForm):
	class Meta:
		model=Ert
		fields='__all__'