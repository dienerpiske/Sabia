# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

#Import's necessarios
from nltk.corpus import stopwords
from nltk import FreqDist
from similarity import similarity, vetores

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
    
    def getTitulosSemelhantes(self):
        artigosBD = Artigo.objects.all()
        artigosSim = []
        
        titulo1 = self.titulo_artigo.lower()
        
        aux1 = vetores(titulo1)

        for  i in range(0,len(artigosBD)):            
            titulo2 = artigosBD[i].titulo_artigo.lower()
            aux2 = vetores(titulo2)
            
            if self.id != artigosBD[i].id and similarity(aux1, aux2):
                artigosSim.append(artigosBD[i])
                
        return artigosSim
    
    def palavrasChaves(self):
        stop = stopwords.words('english')
#         para analisar textos em portugues, habilitar essa linha e comentar a de cima
#         stop = stopwords.words('portuguese')
        palavrasChaves = [] 
        
        #retira as stopwords do texto do artigo que está sendo apresentado
        #retira a ',' e '.' do texto
        textoArtigo =  [i for i in self.texto_artigo.lower().replace(',','').replace('.','').split() if i not in stop]
        
        #apresenta a frequencia de repetição das palavras no corpo do artigo
        freq = FreqDist(textoArtigo)
        
        #separa as quatro palavras mais frequentes
        items = freq.most_common(4)
        
        for i in range(0,len(items)):
            palavrasChaves.append(items[i][0].upper())
            
        return palavrasChaves
        
    

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