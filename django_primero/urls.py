from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hola', include('app.urls')),
    path('', include('app.urls')),
]
