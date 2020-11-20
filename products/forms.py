from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title	= forms.CharField(label='')
	email   = forms.EmailField()
	description = forms.CharField(
				required=False,
				widget=forms.Textarea(
						attrs={
							"class": "new-class two",
							"rows": 10,
							"cols": 5,
							"id": "myid-text",
							"placeholder": "My description"
						}))
	price = forms.DecimalField()

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a valid title")
		if not "news" in title:
			raise forms.ValidationError("This is not a valid title")
		
		return title

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email
		
class RawProductForm(forms.Form):
	title	= forms.CharField(label='')
	description = forms.CharField(
				required=False,
				widget=forms.Textarea(
						attrs={
							"class": "new-class two",
							"rows": 120,
							"cols": 120,
							"id": "myid-text",
							"placeholder": "My description"
						}))
	price = forms.DecimalField()
