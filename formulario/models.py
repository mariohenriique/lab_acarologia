from django.db import models


# Create your models here.

class Colecao(models.Model):
    # criar as variáveis da tabela Darwin Core
    catalogNumber = models.CharField(max_length=50, verbose_name="Tombo",unique=True)
    institutionCode = models.CharField(max_length=5,default="UFMG")
    language = models.CharField(max_length=5,default="pt")
    family = models.CharField(max_length=50, verbose_name="Família", blank=True)
    genus = models.CharField(max_length=50, verbose_name="Gênero", blank=True)
    specie = models.CharField(max_length=50,verbose_name="Espécie",blank=True)
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    modified = models.DateField(auto_now=True)

    def __str__(self):
        # Aparece no campo (mudar para o tombo e alguma outra informação)
        return f"{self.catalogNumber}"