from django.urls.conf import path
from contatos import views

app_name = "contatos"

urlpatterns = [
    path('', views.listaContatosView.as_view(),
        name='contatos'),
    path('lista/', views.listaContatosView.as_view(),
        name='lista-contatos'),
    path('cadastro/', views.insereContatosView.as_view(),
        name='cria-contato')
]