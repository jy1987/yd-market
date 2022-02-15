from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        print(self.cleaned_data)
        print(email, password)
        try:
            user = models.User.objects.get(email=email)
            print(user)
            if user.check_password(password):
                return password
            else:
                self.add_error("password", forms.ValidationError("password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
