import sqlite3
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.http import FileResponse
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd


#Importar as classes do models
from .models import Colecao

# Create your views here.

form = ['catalogNumber','institutionCode','genus','latitude','longitude']

# Adicionar nova exemplar na coleção
class ColecaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Colecao
    fields = form
    template_name = 'formulario/formulario.html'
    success_url = reverse_lazy('confirma_tombo') # procurar como achar o ID

# UPDATE #

class ColecaoUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login')
    model = Colecao
    fields = form
    template_name = 'formulario/formulario.html'
    success_url = reverse_lazy('listar_colecao')

# LIST #

class ColecaoList(ListView):
    model = Colecao
    csv_file = 'static/colecao_UFMGAC.csv'
    form = form
    template_name = 'formulario/listar.html'

class Download(TemplateView):

    def Download(self):
        conn = sqlite3.connect('db.sqlite3')
        db_df = pd.read_sql_query("SELECT * FROM formulario_colecao", conn)
        db_df.to_csv('formulario/colecao_UFMGAC.csv', index=False)
        return FileResponse(open('formulario/colecao_UFMGAC.csv', 'rb'), as_attachment=True)

class TomboList(ListView):
    model = Colecao
    # usar o def request pra colocar mostrar o form da ultima
    template_name = 'formulario/confirma_formulario.html'