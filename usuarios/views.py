from django.shortcuts import render
from django.views.generic import TemplateView
from formulario.models import Colecao

# Create your views here.

class Login(TemplateView):
    template_name = 'login.html'

class PaginaUsuario(TemplateView):
    template_name = 'usuario.html'

class AlteracaoSenha(TemplateView):
    template_name = 'alterar_senha.html'

class AdicionarFactsheets(TemplateView):
    template_name = 'alterar_factsheets.html'

    '''def AtualizaListaChoices(self):
        FAMILY = [(colecao["family"],colecao["family"]) 
                        for colecao in list(Colecao.objects.all().values('family').distinct().order_by("family"))]
        FAMILY_CHOICES = [('Selecione uma Família','Selecione uma Família')]+FAMILY
        return FAMILY_CHOICES'''
    