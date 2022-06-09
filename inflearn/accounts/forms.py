from django import forms
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm  

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'zipcode']


class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(help_text='5 + 5 = ?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer')

        if answer != 6:
            raise forms.ValidationError('땡~!')
        return answer
