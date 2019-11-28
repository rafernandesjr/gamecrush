from django import forms
from .models import User
from django.utils import timezone
import datetime
from django.conf import settings

settings.LANGUAGE_CODE = 'pt-br'

BIRTH_YEAR_CHOICES = [ano for ano in range(1950,2005)]
BIRTH_YEAR_CHOICES.sort(reverse=True)

class UserCreate(forms.ModelForm):
    name = forms.CharField(label='Nome Completo')
    describe = forms.CharField(widget=forms.Textarea, label='Descrição')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmação de Senha')
    birthdate = forms.DateField(widget = forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), label='Data de Nascimento', initial=datetime.datetime.today())
    email = forms.EmailField(label='E-mail')
    class Meta:
        model = User
        fields = ('name', 'birthdate','email','password', 'confirm_password', 'describe')
        help_texts = {
            'password': 'Digite um senha boa de lembrar, mas segura!',
            'confirm_password': 'Por favor digite aqui novamente a sua senha.',
            'email': 'Por favor digite um endereço de e-mail.'
        }
        error_messages = {
            'name': {
                'max_length': 'Esse nome é muito comprido! Precisamos apenas do nome e sobrenome.',
            },
            'email': {
                'required': 'E-mail inválido! Digite um verdadeiro.'
            }
        }

    def clean(self):
        cleaned_data = super(UserCreate, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Senhas digitadas não coincidem")

class UserLogin(forms.ModelForm):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    class Meta:
        model = User
        fields = ('email', 'password')