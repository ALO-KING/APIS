from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

import qrcode
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.contrib.auth.hashers import check_password
import qrcode
from .models import Usuario  

from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import render, redirect
import qrcode
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Categoria


def vistaalumno_view(request):
    return render(request, 'vistaalumno.html') 

def vistaalumnoiti_view(request):
    return render(request, 'vistaalumnoiti.html') 

def vistaalumnoind_view(request):
    return render(request, 'vistaalumnoind.html') 

def vistadocente_view(request):
    return render(request, 'vistadocente.html') 
# Vista para la página de inicio de sesión
def login_view(request):
    return render(request, 'login.html')  # Renderizamos la plantilla login.html

# Vista para la página de inicio de libros (puedes personalizar esta vista según tu necesidad)
def homeView(request):
    return render(request, 'home.html')  # Cambiar el nombre de la plantilla según lo que desees

def book_view(request):
    return render(request, 'book.html')

def category_view(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')

        # Crea una instancia del modelo Docente
        categoria = Categoria(
            codigo=codigo,
            nombre=nombre,
        )

        # Guarda el objeto en la base de datos
        categoria.save()

        
        return redirect('listcategory_view')  
    return render(request, 'category.html')

def bookagregar_view(request):
    return render(request, 'bookagregar.html')

def catalog_view(request):
    return render(request, 'catalog.html')

def advancesettings_view(request):
    return render(request, 'advancesettings.html')

def report_view(request):
    return render(request, 'report.html')

def loan_view(request):
    return render(request, 'loan.html')

def loanpending_view(request):
    return render(request, 'loanpending.html')

def loanreservation_view(request):
    return render(request, 'loanreservation.html')

def section_view(request):
    return render(request, 'section.html')

def Olvcontraseña_view(request):
    return render(request, 'Olvcontraseña.html')

def restablecerContraseña_view(request):
    return render(request, 'restablecerContraseña.html')

def fisicos_view(request):
    return render(request, 'fisicos.html')

def infobook_view(request):
    return render(request, 'infobook.html')

def listadmin_view(request):
    # Obtenemos todos los administradores desde el modelo Usuario filtrando por rol
    administradores = Usuario.objects.filter(rol='admin')
    return render(request, 'listadmin.html', {'administradores': administradores})

def listpersonal_view(request):
    # Obtenemos todos los usuarios con rol 'personal'
    personal = Usuario.objects.filter(rol='personal')
    return render(request, 'listpersonal.html', {'personal': personal})

def liststudent_view(request):
    # Obtenemos todos los usuarios con rol 'estudiante'
    estudiantes = Usuario.objects.filter(rol='estudiante')
    return render(request, 'liststudent.html', {'estudiantes': estudiantes})

def listteacher_view(request):
    # Obtenemos todos los usuarios con rol 'docente'
    docentes = Usuario.objects.filter(rol='docente')
    return render(request, 'listteacher.html', {'docentes': docentes})


def listcategory_view(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST' and 'delete' in request.POST:
        categoria_id = request.POST.get('categoria_id')
        categoria = get_object_or_404(Categoria, id=categoria_id)

        # Preguntar si realmente desea eliminar
        if 'confirm_delete' in request.POST:
            categoria.delete()
            messages.success(request, 'Categoría eliminada exitosamente.')
        else:
            messages.warning(request, '¿Estás seguro de que deseas eliminar esta categoría?')
            return render(request, 'listcategory.html', {'categorias': categorias, 'confirm_delete': True, 'categoria_id': categoria_id})
    
    return render(request, 'listcategory.html', {'categorias': categorias})


def homeView(request):
    if request.method == 'POST':
        identificador = request.POST.get('identificador', '').strip()
        password = request.POST.get('password', '').strip()

        # Verificar que el identificador y la contraseña no sean vacíos
        if not identificador:
            messages.error(request, 'Por favor, ingrese su matrícula o número de trabajador.')
            return render(request, 'login.html')

        if not password:
            messages.error(request, 'Por favor, ingrese su contraseña.')
            return render(request, 'login.html')

        try:
            # Validar identificador y obtener el usuario correspondiente
            if len(identificador) == 10:  # Se asume que es una matrícula
                usuario = Usuario.objects.get(matricula=identificador, rol='estudiante')
            elif len(identificador) == 3:  # Se asume que es un número de trabajador
                usuario = Usuario.objects.get(numero_trabajador=identificador, rol__in=['admin', 'docente', 'personal'])
            else:
                messages.error(request, 'El identificador debe ser una matrícula de 10 dígitos o un número de trabajador de 3 dígitos.')
                return render(request, 'login.html')

            # Verificar la contraseña
            if check_password(password, usuario.password):
                # Guardar datos en la sesión
                request.session['usuario_id'] = usuario.id
                request.session['rol'] = usuario.rol
                request.session['programa_educativo'] = usuario.programa_educativo

                # Generar el código QR
                qr = qrcode.QRCode(version=1, box_size=10, border=5)

                if usuario.rol == 'estudiante':
                    qr.add_data(usuario.matricula)
                else:
                    qr.add_data(usuario.numero_trabajador)

                qr.make(fit=True)
                img = qr.make_image(fill_color='black', back_color='white')

                # Guardar la imagen del QR
                qr_file_name = f'qr_{usuario.id}.png'
                img_io = ContentFile(img.tobytes())
                qr_file_path = default_storage.save(qr_file_name, img_io)
                
                usuario.qr_code = qr_file_path
                usuario.save()

                # Redirigir según el rol del usuario
                if usuario.rol == 'admin':
                    messages.success(request, 'Inicio de sesión exitoso como Administrador')
                    return redirect('book')
                elif usuario.rol == 'docente':
                    messages.success(request, 'Inicio de sesión exitoso como Docente')
                    return redirect('vistadocente')
                elif usuario.rol == 'personal':
                    messages.success(request, 'Inicio de sesión exitoso como Personal')
                    return redirect('book')
                elif usuario.rol == 'estudiante':
                    messages.success(request, 'Inicio de sesión exitoso como Estudiante')
                    if usuario.programa_educativo == 'Ingeniería en Tecnologías de la Información':
                        return redirect('vistaalumnoiti')
                    elif usuario.programa_educativo == 'Ingeniería Industrial':
                        return redirect('vistaalumnoind')
                    else:
                        messages.error(request, 'Programa educativo no reconocido.')
                        return render(request, 'login.html')
            else:
                messages.error(request, 'Contraseña incorrecta.')

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado. Verifique su matrícula o número de trabajador.')
        except Exception as e:
            messages.error(request, f'Ocurrió un error: {str(e)}')

    return render(request, 'login.html')













