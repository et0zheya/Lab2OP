from django import forms
from .models import *
class add_notes(forms.ModelForm):
	class Meta:
		model = notes  
		fields = ['title']
		widgets = {
			
			'title' :forms.TextInput(attrs={'placeholder':'Input the title:', 'class':'form-control'}),
		}
		
class add_comment(forms.Form):
			
	single_comment = forms.CharField(
		widget=forms.TextInput(attrs={'placeholder':'Input your comment:', 'class':'form-control'}))
		