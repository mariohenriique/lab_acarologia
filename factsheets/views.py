from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Max,Min
from django.utils.safestring import mark_safe

from folium import Marker,Map

from formulario.models import Colecao
from .models import InformacaoFamilias

# Create your views here.

class FactSheets(TemplateView):
    template_name = 'factsheets.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['familia'] = Colecao.objects.all().values('family').distinct().order_by('family')
        return context

class FactSheetsFamilia(TemplateView):
    template_name = 'factsheets_familia.html'
    def qual_familia(self):
        return self.kwargs['family']

    # Função que gera o mapa

    def fazer_mapa(self):
        family = self.kwargs['family']

        # chamar apenas os objetos de determinada família
        colecaos = Colecao.objects.filter(family=family)

        # Lista com o maior e menor valor de latitude e longitude
        latitude = list(Colecao.objects.filter(family=family).aggregate(Max('latitude'),Min('latitude')).values())
        longitude = list(Colecao.objects.filter(family=family).aggregate(Max('longitude'),Min('longitude')).values())
        
        # média
        latitudemedia = (sum(latitude))/2
        longitudemedia = (sum(longitude))/2

        mapa_familia = Map(location=[latitudemedia,longitudemedia],zoom_start=4,tiles='Stamen Terrain')
        
        for colecao in colecaos:
            lat = colecao.latitude
            lon = colecao.longitude
            Marker([lat, lon],popup = colecao.language).add_to(mapa_familia)
        return mapa_familia._repr_html_()
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # Gera a somente a div do mapa
        context['map'] = mark_safe(self.fazer_mapa())
        return render(request,self.template_name,context)

    def get_context_data(self, **kwargs):
        family = self.kwargs['family']
        context = super().get_context_data(**kwargs)
        generoscolecao = Colecao.objects.filter(family=family).order_by("genus")
        context['genero'] = generoscolecao.values('genus').distinct()
        context['especie'] = generoscolecao.order_by("specie").values('genus','specie').distinct()
        context['familia'] = InformacaoFamilias.objects.filter(familia=family)
        return context