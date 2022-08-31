from django.urls import path
from . import views

urlpatterns = [
    path('bemvindo/', views.bemvindo),
    path('produtos/', views.produtos_listar),
    path('produtos/<int:id>', views.produto_detalhe)
]
