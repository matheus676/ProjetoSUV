from django.db import models

# Create your models here.    


class LoteDeVacina(models.Model):
    fabricante = models.CharField('Fabricante', max_length=50)
    quantidade = models.IntegerField('Quantidade')
    data_de_validade = models.DateField('Data de Validade')
    class Meta:
        verbose_name = 'Posto de Saúde'
        verbose_name_plural = 'Postos de Saúde'
        ordering =['id']

    def __str__(self):
        return self
    
class Vacina(models.Model):
    nome = models.CharField('Nome', max_length=50)
    dose_padrao = models.DecimalField('Dose Padrão', max_digits=4, decimal_places=4)
    lote_de_vacina = models.ForeignKey(LoteDeVacina,verbose_name='Lote de Vacina', on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Posto de Saúde'
        verbose_name_plural = 'Postos de Saúde'
        ordering =['id']

    def __str__(self):
        return self
