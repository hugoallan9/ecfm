from django.conf.urls import url

from .views import procesar_permiso

urlpatterns = [
    url(r'^permisos/generar_nombramiento$',procesar_permiso),
]
