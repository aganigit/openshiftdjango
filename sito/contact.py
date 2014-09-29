from django import forms 

# A simple contact form with five fields.
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    cognome = forms.CharField(max_length=100)
    data = forms.DateField()
    citta = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())
    cc_myself = forms.BooleanField(required=False)