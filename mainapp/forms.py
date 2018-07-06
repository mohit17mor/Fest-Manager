from django import forms
from .models import Contract

class LoginForm(forms.Form):
    user_types = (
        ('organiser', 'organiser'),
        ('vendor', 'vendor'),
    )
    type_of_user = forms.ChoiceField(choices = user_types)
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class CreateContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'contract_type',
            'description',
            'price',
        ]
