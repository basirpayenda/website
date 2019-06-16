from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

