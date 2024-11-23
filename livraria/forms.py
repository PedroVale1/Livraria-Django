from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book

class SingUpForm(UserCreationForm):
  email = forms.EmailField(label="", widget=forms.TextInput(
    attrs={
      'class': 'form-control', 'placeholder': 'E-mail'
    }
  ))
  first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
    attrs={
      'class': 'form-control', 'placeholder': 'First Name'
    }
  ))
  last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(
    attrs={
      'class': 'form-control', 'placeholder': 'Last Name'
    }
  ))

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

  def __init__(self, *args, **kwargs):
    super(SingUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    self.fields['username'].label = ''
    self.fields['username'].help_text = '''
      <span class = "form-text text-muted">
         <small>Obrigatório. 150 caracteres ou menos. Letras, dígitos e alguns caracteres</small>
      </span>
    '''

    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '''
      <ul class = "form-text text-muted small">
         <li>Senha deve ser única.</li>
         <li>Senha deve conter pelo menos 8 caracteres.</li>
         <li>Senha não deve ser totalmente numérica.</li>
      </ul>
    '''

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '''
      <span class = "form-text text-muted">
         <small>Digite a mesma senha digitada no campo anterior</small>
      </span>
    '''


class AddBookForm(forms.ModelForm):
    title = forms.CharField(required=True,
          widget=forms.widgets.TextInput(
            attrs={"placeholder": "Título Livro", "class": "form-control"}
          ), label="")
    description = forms.CharField(required=True,
                widget=forms.widgets.Textarea(
                  attrs={"placeholder": "Descrição Livro", "class": "form-control"}
                ), label="")
    year = forms.IntegerField(required=True,
          widget=forms.widgets.NumberInput(
            attrs={"placeholder": "Ano Livro", "class": "form-control"}
          ), label="")
    genre = forms.CharField(required=True,
          widget=forms.widgets.TextInput(
            attrs={"placeholder": "Gênero Livro", "class": "form-control"}
          ), label="")
    value = forms.IntegerField(required=True,
          widget=forms.widgets.NumberInput(
            attrs={"placeholder": "Valor Livro", "class": "form-control"}
          ), label="")

    class Meta:
        model = Book
        fields = ('title', 'description', 'year', 'genre', 'value')
