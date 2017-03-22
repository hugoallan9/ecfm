from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.http import HttpResponse
from .forms import Permiso
# Create your views here.

def procesar_permiso(request):
    if request.method == 'POST':
        form = Permiso(request.POST)
        if form.is_valid():
            fichero = open('machote.tex','w')
            registro = form.cleaned_data['registro_personal']
            fichero.write('Su men: ' + str(registro) )
            template = loader.get_template('base.html')
            context ={}
            return HttpResponse(template.render(request))
    else:
        form = Permiso()

    return render(request, 'permiso/permiso.html', {'form':form} )
