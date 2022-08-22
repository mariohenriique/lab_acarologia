from django.db import models
from datetime import datetime
from formulario.models import Colecao

# Create your models here.

# Criar os campos da página factsheets

class InformacaoFamilias(models.Model):
    FAMILY = [(colecao["family"],colecao["family"]) 
                        for colecao in list(Colecao.objects.all().values('family').distinct().order_by("family"))]
    FAMILY_CHOICES = [('Selecione uma Família','Selecione uma Família')]+FAMILY

    ano_choice = [(r,r) for r in range(1980,datetime.now().year+1)]
    familia = models.CharField(max_length=50, choices=FAMILY_CHOICES,
                                verbose_name='Família',default='Seleciona uma Família',unique=True)
    imagem = models.FileField(upload_to='static/factsheets',blank=True)
    autor = models.CharField(max_length=50)
    ano = models.IntegerField(choices=ano_choice,help_text="Selecione o ano",default=ano_choice[-1])
    diagnoses = models.TextField(verbose_name="Diagnoses")
    dados_geneticos = models.URLField(max_length=200,verbose_name="Dados genéticos")

    def __str__(self):
        return f"{self.familia}"

class Imagens(models.Model):
    post = models.ForeignKey(InformacaoFamilias,on_delete=models.CASCADE)
    imagens = models.ImageField(upload_to='static/factsheets')