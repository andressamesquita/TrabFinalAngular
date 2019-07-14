from django.db import models

class Apicultor(models.Model):
   
    nome = models.CharField(max_length=255, null=False)
    qtd_apiarios = models.IntegerField()
    tipo_criador = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.nome
    
    
class Apiario(models.Model):
    qtd_colmeias = models.IntegerField()
    apicultor = models.CharField(max_length=255, null=False)
    localizacao = models.CharField(max_length=255, null=False)
    

    def __str__(self):
        return 'Api '+ str(self.id) + ' - ' + str(self.apicultor)
    
    def excluir_apiario(self):
        self.delete() 

   
class CaixaRacional(models.Model):
    apiario = models.CharField(max_length=255, null=False)
    identificador = models.CharField(max_length=255, null=False)
    especie = models.CharField(max_length=255, null=False)
   
    def excluir_caixa_racional(self):
        self.delete() 
    

class Perda(models.Model):
       
    tipo_perda = models.CharField(max_length=255, null=False)
    qtd_colmeias_perdidas = models.IntegerField()
    data_registro_perda = models.DateTimeField(auto_now_add=True)
    especie_perdida = models.CharField(max_length=255, null=False)
    #foto_perda = models.FileField(required=False)
    apiario = models.CharField(max_length=255, null=False)

    class Meta:
        ordering = ['-data_registro_perda']

    def excluir_perda(self):
        self.delete()