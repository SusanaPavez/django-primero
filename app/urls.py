from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	  
    path('hola/<str:nombre>', views.saludar),	 
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path ('', views.index),        # el ' ' significa que cada vez que un usuario ejecute una ruta vacía, se irá a la vista views.index
#     path('hola/<str:nombre>', views.saludar),   # esto significar que cada vez que haya una solicitud que comience por "hola/nombre",
#                                         # ejecutará la función  "saludar", la cual está en views.py de la carpeta con el nombre de proyecto
# ]