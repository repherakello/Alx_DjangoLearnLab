from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    published_date = forms.DateField()
