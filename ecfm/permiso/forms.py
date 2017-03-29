#-*-encoding:utf8-*-
from django import forms
import datetime
MY_CHOICES = (
    ('1', 'Docencia'),
    ('2', 'Investigación'),
    ('3', 'Extensión'),
)
class Permiso(forms.Form):
    registro_personal = forms.IntegerField()
    nombre_profesional = forms.CharField()
    nombre_evento = forms.CharField()
    lugar_evento = forms.CharField()
    fecha_evento = forms.DateField(initial=datetime.date.today)
    Tipo_de_evento = forms.ChoiceField(choices=MY_CHOICES)
