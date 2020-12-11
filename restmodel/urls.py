from django.urls import path
from.views import jsonfunction,lista,detalle,carga,editar,eliminar
urlpatterns = [
    path("api/",jsonfunction,name="jsonfunction"),
    path("lista/",lista,name="lista"),
    path("detalle/<int:id>/",detalle,name="detalle"),
    path("carga/",carga,name="carga"),
    path("eliminar/<int:id>/",eliminar,name="elimina"),
    path("editar/<int:id>/",editar,name="edita"),
]
