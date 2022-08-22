from django.urls import path

# importar as classes no pacote views
from .views import ColecaoCreate,ColecaoUpdate,ColecaoList,TomboList,Download

urlpatterns = [
    #path('endereço/', PacoteView.as_view(),name='nome_da_url'),
    path('cadastrar/colecao/',ColecaoCreate.as_view(),name='cadastrar_colecao'),
    path('editar/colecao/<int:pk>/',ColecaoUpdate.as_view(),name='editar_colecao'),
    path('listar/colecao/',ColecaoList.as_view(),name='listar_colecao'),
    path('confirma/tombo/',TomboList.as_view(),name='confirma_tombo'),
    path('download/',Download.Download,name='baixa'),
]