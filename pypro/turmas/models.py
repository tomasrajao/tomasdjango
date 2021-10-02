from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
from pypro.base.models import User


class Turma(models.Model):
    nome = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    inicio = models.DateField()
    fim = models.DateField()
    alunos = models.ManyToManyField(get_user_model(), through='Matricula')

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['usuario', 'turma']
        ordering = ['turma', 'data']

    def __str__(self):
        return User.get_short_name(self.usuario)
