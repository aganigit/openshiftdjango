from django import forms
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.template import loader
from django.utils.translation import ugettext_lazy as _


class BaseEmailFormMixin(object):
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email for _, email in settings.MANAGERS]

    subject_template_name = 'contact_form/email_subject.txt'
    message_template_name = 'contact_form/email_template.txt'

    def get_message(self):
        return loader.render_to_string(self.message_template_name, self.get_context())

    def get_subject(self):
        subject = loader.render_to_string(self.subject_template_name, self.get_context())
        return ''.join(subject.splitlines())

    def get_context(self):
        """
        Context sent to templates for rendering include the form's cleaned
        data and also the current Request object.
        """
        if not self.is_valid():
            raise ValueError("Cannot generate Context when form is invalid.")
        return dict(request=self.request, **self.cleaned_data)

    def get_email_headers(self):
        """
        Subclasses can replace this method to define additional settings like
        a reply_to value.
        """
        return None

    def get_recipient_list(self):
        return self.recipient_list

    def get_from_email(self):
        return self.from_email

    def get_message_dict(self):
        message_dict = {
            "from_email": self.get_from_email(),
            "to": self.get_recipient_list(),
            "subject": self.get_subject(),
            "body": self.get_message(),
        }
        headers = self.get_email_headers()
        if headers is not None:
            message_dict['headers'] = headers
        return message_dict

    def send_email(self, request, fail_silently=False):
        self.request = request
        return EmailMessage(**self.get_message_dict()).send(fail_silently=fail_silently)


class ContactForm(forms.Form, BaseEmailFormMixin):
    """
    Subclass this and declare your own fields.
    """


class ContactModelForm(forms.ModelForm, BaseEmailFormMixin):
    """
    You'll need to declare the model yourself.
    """


class BasicContactForm(ContactForm):
    """
    A very basic contact form you can use out of the box if you wish.
    """
    nome = forms.CharField(label=_(u'Nome:'), max_length=100)
    cognome = forms.CharField(label=_(u'Cognome:'), max_length=100)
    telefono = forms.CharField(label=_(u'Telefono:'), max_length=100)
    fax = forms.CharField(label=_(u'Fax:'), max_length=100)
    email = forms.EmailField(label=_(u'email:'), max_length=200)
    citta = forms.CharField(label=_(u'Citta:'), max_length=100)
    indirizzo = forms.CharField(label=_(u'Indirizzo:'), max_length=100)
    messaggio = forms.CharField(label=_(u'Messaggio:'), widget=forms.Textarea())

    def get_email_headers(self):
        return {'Reply-To': self.cleaned_data['email']}
