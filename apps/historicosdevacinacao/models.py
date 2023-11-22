from django.db import models
from pacientes.models import Paciente
from vacinas.models import Vacina
from atendentes.models import Atendente
# Create your models here.
class HistoricoDeVacinacao(models.Model):
    paciente = models.ForeignKey(Paciente,verbose_name='Paciente', on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina,verbose_name='Vacina' ,on_delete=models.CASCADE)
    atendente = models.ForeignKey(Atendente,verbose_name='Atendente', on_delete=models.CASCADE)
    ESCOLHAS_STATUS = (
        ('Vacinação Agendada', 'Vacinação Agendada'),
        ('Vacinação Realizada', 'Vacinação Realizada'),
        ('Vacinação Pendente', 'Vacinação Pendente'),
    )
    status_de_vacinacao =  models.CharField('Status',max_length=20,choices=ESCOLHAS_STATUS,null=True, blank=True, default='Vacinação Pendente')
    class Meta:
        verbose_name = 'Histórico de Vacinação'
        verbose_name_plural = 'Históricos de Vacinação'
        ordering =['id']

    def __str__(self):
        return self
    