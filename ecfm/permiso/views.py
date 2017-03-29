#-*-encoding:utf8-*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from .forms import Permiso
import datetime
import locale
# Create your views here.
formato_local = "%x "
locale.setlocale(locale.LC_ALL, "es_GT.utf8")

def procesar_permiso(request):
    if request.method == 'POST':
        form = Permiso(request.POST)
        if form.is_valid():
            fichero = open('permiso/machote/datos.tex','w')
            registro = form.cleaned_data['registro_personal']
            fichero.write('\\def \\registro : { ' + str(registro) + ' }\n' )
            nombre = form.cleaned_data['nombre_profesional']
            fichero.write('\\def \\nombre : { ' + str(nombre) + ' }\n' )
            nombre_evento = form.cleaned_data['nombre_evento']
            fichero.write('\\def \\evento : { ' + str(nombre_evento) + ' }\n' )
            fecha = form.cleaned_data['fecha_evento']
            fichero.write('\\def \\dias : { ' + datetime.datetime.strftime(fecha,"%d %B de %Y") + ' }\n' )
            lugar = form.cleaned_data['lugar_evento']
            fichero.write('\\def \\lugar : { ' + str(lugar) + ' }\n' )
            template = loader.get_template('base.html')
            context ={}
            return HttpResponse(template.render(request))
    else:
        form = Permiso()

    return render(request, 'permiso/permiso.html', {'form':form} )
