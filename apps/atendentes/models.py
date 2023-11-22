from django.db import models
from postodesaude.models import PostoDeSaude
# Create your models here.
class Atendente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    especialidade = models.CharField('Especialidade', max_length=50)
    posto_de_saude = models.ForeignKey(PostoDeSaude,verbose_name='Posto de Saúde',on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Atendente'
        verbose_name_plural = 'Atendentes'
        ordering =['id']

    def __str__(self):
        return self