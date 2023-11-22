from django.db import models
from postodesaude.models import PostoDeSaude
from pacientes.models import Paciente
# Create your models here.
class Agendamento(models.Model):
    datahora = models.DateTimeField('Data e Hora')
    postodesaude = models.ForeignKey(PostoDeSaude, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Agendamentos'
        verbose_name_plural = 'Agendamentos'
        ordering =['id']

    def __str__(self):
        return self