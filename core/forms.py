from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Classes CSS do Tailwind para os inputs ficarem bonitos
STYLE_INPUT = "w-full bg-[#082640] border border-slate-600/50 rounded-xl p-3 text-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all placeholder-slate-400"

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': STYLE_INPUT, 'placeholder': 'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': STYLE_INPUT, 'placeholder': 'Senha'}))

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica o estilo em todos os campos automaticamente
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': STYLE_INPUT})