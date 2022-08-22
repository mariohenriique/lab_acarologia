from django.urls import path,re_path

# Importar classes do pacote views
from .views import FactSheets,FactSheetsFamilia

urlpatterns = [
    #path('endereço/', PacoteView.as_view(),name='nome_da_url'),
    path('factsheets/',FactSheets.as_view(),name='factsheets'),
    re_path(r'factsheets/(?P<family>\w+)/$',FactSheetsFamilia.as_view(),name='factsheetsfamilia'),
]