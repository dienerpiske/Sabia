# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User)
    informacoes_usuario = models.TextField(max_length = 500)
    
    class Meta:
        db_table = 'Usuario'

class Artigo(models.Model):
    titulo_artigo = models.TextField()
    texto_artigo = models.TextField()
    tags_artigo = models.TextField()
    
    class Meta:
        db_table = 'Artigo'
        
    def getArtSemelhantes(self):
        return Artigo.objects.all() #mudar isso usando o comparados por tag

class Fichamento(models.Model):
    titulo_fichamento = models.TextField()
    likes_fichamento = models.IntegerField()
    usuario = models.ForeignKey(User)
    #usuario_id = models.IntegerField()
    artigo = models.ForeignKey(Artigo)
    
    class Meta:
        db_table = 'Fichamento'
        
    def __unicode__(self):
        return self.titulo_fichamento
    
    def getResumo(self):
        marcacoes = self.marcacao_set.all()
        resumo = "<h2>"+self.titulo_fichamento+"</h2>"
        for m in marcacoes:
            resumo += "<h4>"+m.titulo_marcacao+"</h3>"
            resumo += "<h6>"+m.texto_marcacao+"</h6>"
        return resumo

class Marcacao(models.Model):
    titulo_marcacao = models.TextField()
    texto_marcacao = models.TextField()
    fichamento = models.ForeignKey(Fichamento)
    
    class Meta:
        db_table = 'Marcacao'
        
    def __unicode__(self):
        return self.titulo_marcacao

#class Ranking(models.Model):
#    usuario = models.ForeignKey(Usuario)
#    colocacao_atual = models.IntegerField()
#    
#    class Meta:
#        db_table = 'Ranking'

#class Similaridade(models.Model):
#    corpus = models.TextField()
#    
#    class Meta:
#        db_table = 'Similaridade'
#