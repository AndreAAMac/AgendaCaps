from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    OPCOES = [
        ('consulta', 'Consulta'),
        ('retorno', 'Retorno'),
    ]
    tipo = models.CharField(max_length=10, choices=OPCOES)
    
    def __str__(self):
        return f"{self.nome} ({self.cidade}) - {self.tipo}"