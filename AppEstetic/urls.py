from django.urls import path
from AppEstetic.views import*


urlpatterns=[
    path('Esteticista/',esteticista, name="esteticista"),
    path('cosmetologa/',cosmetologa, name="cosmetologa"),
    path('manicura/',manicura, name="manicura"),
    path("",inicio, name="inicio"),
    path('contacto/',contacto, name="contacto"),
    path('paciente_Formulario/',paciente_Formulario, name='paciente_Formulario'),
    path('busquedaContactos/',busquedaContactos, name="busquedaContactos"),
    path('resultadoBusqueda/', buscar, name="resultadoBusqueda"),
    
  
]