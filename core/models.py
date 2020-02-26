from django.db import models
from django.contrib.auth.models import User


class Clube(models.Model):
    chave = models.CharField(null=False, blank=False)
    nome = models.CharField(null=False, blank=False)
    distrito = models.IntegerField(null=False, blank=False)
    presidente = models.ForeignKey(User)


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    email = models.CharField(null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    clube = models.ForeignKey(Clube)
    endereco = models.CharField()


class ExperienciaProfissional(models.Model):
    user = models.ForeignKey(User)
    cargo = models.CharField()
    empresa = models.CharField()
    localidade = models.CharField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    descricao = models.TextField()


class FormacaoAcademica(models.Model):
    user = models.ForeignKey(User)
    instituicao = models.CharField()
    formacao = models.CharField()
    area_estudo = models.CharField()
    atividades_desenvolvidas = models.TextField()
    ano_inicio = models.CharField()
    ano_fim = models.CharField()


class Linguas(models.Model):
    user = models.ForeignKey(User)
    nome = models.CharField()
    nivel = models.CharField()


class Conversa(models.Model):
    user_one = models.ForeignKey(User)
    user_two = models.ForeignKey(User)


class Mensagem(models.Model):
    conversa = models.ForeignKey(Conversa)
    texto = models.CharField()
    created_at = models.DateTimeField(auto_now=True)
    enviado_por = models.ForeignKey(User)


class Conexao(models.Model):
    user_one = models.ForeignKey(User)
    user_two = models.ForeignKey(User)