from django.urls import path 
from . import views


urlpatterns = [
    path('lab', views.lab, name='lab'),
    path('formadd/', views.formadd, name='formadd'),
    path('editar/<id>', views.editar),
    path('editarlab/', views.editarlab),
    path('eliminar/<id>', views.eliminar),
]