# -*- coding: utf-8 -*-
from django.db import models

class Usuario(models.Model):
    nome_usuario  = models.TextField()
    email_usuario = models.CharField(max_length = 200)
    login_usuario = models.CharField(max_length = 15)
    senha_usuario = models.CharField(max_length = 20)
    
    class Meta:
        db_table = 'Usuario'

class Artigo(models.Model):
    titulo_artigo = models.TextField()
    texto_artigo = models.TextField()
    
    class Meta:
        db_table = 'Artigo'

class Fichamento(models.Model):
    titulo_topico = models.TextField()
    texto_topico = models.TextField()
    usuario = models.ForeignKey(Usuario)
    artigo = models.ForeignKey(Artigo)
    
    class Meta:
        db_table = 'Fichamento'
        
    def __unicode__(self):
        return self.titulo_topico
    
class Ranking(models.Model):
    usuario = models.ForeignKey(Usuario)
    colocacao_atual = models.IntegerField()
    
    class Meta:
        db_table = 'Ranking'

class Similaridade(models.Model):
    corpus = models.TextField()
    
    class Meta:
        db_table = 'Similaridade'