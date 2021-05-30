from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Doctor, Patient


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(
        choices=(("doctor", "Doctor"), ("patient", "Patient")), required=True
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            if self.cleaned_data["user_type"] == "doctor":
                Doctor.objects.create(user=user)
            if self.cleaned_data["user_type"] == "patient":
                Patient.objects.create(user=user)
        return user
