from django.urls import path
from .views import IndexView, MenuView

urlpatterns = [
    #path('endereço/', MinhaView.as_view(), name='nome_da_url'),
    path('', IndexView.as_view(), name='paginas-index'),
    path('gerenciamento/', MenuView.as_view(), name='paginas-menu'),
]