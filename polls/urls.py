from django.urls import path

from .views import Pagina_Inicial

urlpatterns = [
    path('', Pagina_Inicial, name='Pagina_Inicial' ),
]