from django import forms
import datetime

class Permiso(forms.Form):
    registro_personal = forms.IntegerField()
    nombre_profesional = forms.CharField()
    nombre_evento = forms.CharField()
    fecha_evento = forms.DateField(initial=datetime.date.today)

    
