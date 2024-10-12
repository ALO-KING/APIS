from django.urls import path
from .views import homeView # Importamos las vistas que vamos a usar
from .views import book_view,category_view,bookagregar_view,catalog_view,advancesettings_view,listadmin_view,listpersonal_view, report_view, loan_view,loanpending_view,loanreservation_view, liststudent_view,listteacher_view, section_view, Olvcontraseña_view, restablecerContraseña_view,fisicos_view,infobook_view,listcategory_view,vistaalumno_view, vistadocente_view,vistaalumnoind_view, vistaalumnoiti_view
urlpatterns = [
    path('login/', homeView, name='login'),  # Ruta para el home (puedes cambiarlo según tu necesidad)
    path('book/', book_view, name='book'), 
    path('category/', category_view, name='category'),
    path('bookagregar/', bookagregar_view, name='bookagregar'),
    path('catalog/', catalog_view, name='catalog'),
    path('advancesettings/', advancesettings_view, name='advancesettings'),
    path('listadmin/', listadmin_view, name='listadmin_view'),
    path('listpersonal/', listpersonal_view, name='listpersonal_view'),
    path('report/', report_view, name='report'),
    path('loan/', loan_view, name='loan'),
    path('loanpending/', loanpending_view, name='loanpending'),
    path('loanreservation/', loanreservation_view, name='loanreservation'),
    path('liststudent/', liststudent_view, name='liststudent_view'),
    path('listteacher/', listteacher_view, name='listteacher_view'),
    path('listcategory/', listcategory_view, name='listcategory_view'),
    path('section/', section_view, name='section'),
    path('Olvcontraseña/', Olvcontraseña_view, name='Olvcontraseña'),
    path('restablecerContraseña/', restablecerContraseña_view, name='restablecerContraseña'),
    path('fisicos/', fisicos_view, name='fisicos'),
    path('infobook/', infobook_view, name='infobook'),
    path('vistaalumno/', vistaalumno_view, name='vistaalumno'),
    path('vistaalumnoind/', vistaalumnoind_view, name='vistaalumnoind'),
    path('vistaalumnoiti/', vistaalumnoiti_view, name='vistaalumnoiti'),
    path('vistadocente/', vistadocente_view, name='vistadocente'),
   

    
]

