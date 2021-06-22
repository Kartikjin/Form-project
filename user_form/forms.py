from django import forms
from .models import CustomUser
from django.core.mail import send_mail
from internship_project import settings

# Create your Forms here

class UserCreationForm(forms.ModelForm):
    dob = forms.DateField()
    class Meta:
        model = CustomUser
        fields = '__all__'     

    def save(self):
        user = super().save()
        subject = "User Form Submitted"
        message = "Form Has Been Submitted Succesfully"
        sender = settings.EMAIL_HOST_USER
        recipient = [self.cleaned_data['email']]
        send_mail(subject, message, sender, recipient)
        return user

