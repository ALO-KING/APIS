from django.db import models


class Usuario(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('docente', 'Docente'),
        ('estudiante', 'Estudiante'),
        ('personal', 'Personal'),
    ]
    
    # Campos comunes
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)  # Contraseña hasheada
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_finalizacion = models.DateField(blank=True, null=True)
    estado = models.BooleanField(default=True)  # Indica si está activo
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    
    # Campo para diferenciar roles
    rol = models.CharField(max_length=10, choices=ROLES)
    
    # Campos específicos
    numero_trabajador = models.CharField(max_length=15, blank=True, null=True)  # Solo para admin, docente y personal
    matricula = models.CharField(max_length=10, blank=True, null=True)  # Solo para estudiantes
    programa_educativo = models.CharField(max_length=100, blank=True, null=True)  # Solo para estudiantes

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.get_rol_display()}"
    

class Categoria(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
