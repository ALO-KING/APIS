from django import forms
from .models import Usuario, Categoria
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError


class UsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirmar Contraseña')

    class Meta:
        model = Usuario
        fields = [
            'rol', 'username', 'password', 'confirm_password',
            'nombres', 'apellidos', 'telefono',
            'fecha_inicio', 'fecha_finalizacion',
            'numero_trabajador', 'matricula', 'programa_educativo',
            'qr_code'
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        rol = cleaned_data.get('rol')
        numero_trabajador = cleaned_data.get('numero_trabajador')
        matricula = cleaned_data.get('matricula')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Verificar contraseñas coincidan
        if password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden.")

        # Validaciones según el rol
        if rol in ['admin', 'docente', 'personal']:
            if not numero_trabajador:
                raise ValidationError("El número de trabajador es requerido para este rol.")
        elif rol == 'estudiante':
            if not matricula:
                raise ValidationError("La matrícula es requerida para el rol de estudiante.")
            if not cleaned_data.get('programa_educativo'):
                raise ValidationError("El programa educativo es requerido para el rol de estudiante.")

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.password = make_password(self.cleaned_data['password'])
        if commit:
            usuario.save()
        return usuario


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nombre', 'codigo'
        ]
    def save(self, commit=True):
        # Obtiene la instancia original
        categoria = super(CategoriaForm, self).save(commit=False)
        # Hashea la contraseña antes de guardar
        categoria.password = make_password(categoria.password)  # Asegúrate de importar make_password
        if commit:
            categoria.save()
        return categoria
    
class LoginForm(forms.Form):
    numero_trabajador = forms.CharField(label='Número de Trabajador', max_length=10)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)