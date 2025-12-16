from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        
        

        fields = [ 'username', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'last_login', 'date_joined', 'cargo', 'telefone']