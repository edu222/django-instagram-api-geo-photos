from django import forms
#models form forms.ModelForm alternative

class SearchLocationsForm(forms.Form):
	lat = forms.FloatField(max_value=90, min_value=-90)
	lng = forms.FloatField(max_value=180, min_value=-180)
	distance = forms.FloatField()
