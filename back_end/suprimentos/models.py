from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DadosCadModel(models.Model):
    id_user_cad = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_user_cad')
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,blank=True, related_name='%(class)s_user_alt')
    dt_alt = models.DateField(null=True, blank=True, auto_now=True)

    class Meta:
        abstract = True


class Fornecedores(DadosCadModel):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(null=False, max_length=60)
    cnpj = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=60, unique=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    
    class Meta:
        ordering = ['razao_social']
        db_table = "Fornecedores"
        verbose_name_plural = 'Fornecedores'

    def __str__(self) -> str:
        return self.razao_social 

class Projetos(DadosCadModel):
    id_projeto = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    dt_inicio_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField()
    dt_alt = models.DateField()
    
    class Meta:
        ordering = ['titulo']
        db_table = "Projetos"
        verbose_name_plural = 'Projetos'

    def __str__(self) -> str:
        return self.titulo


class NaturezasDespesa(models.Model):
    id_natureza_despesa = models.AutoField(primary_key=True)
    cod_natureza_despesas = models.CharField(max_length=8)
    desc_natureza_despesa = models.CharField(max_length=60)

    class Meta:
        ordering = ["desc_natureza_despesa"]
        db_table = "NaturezasDespesa"
        verbose_name_plural = "Naturezas Despesas"

    def __str__(self) -> str:
        return self.desc_natureza_despesa

    
class Ordens(DadosCadModel):
    id_ordem = models.AutoField(primary_key=True)
    id_projeto = models.ForeignKey(Projetos, on_delete=models.CASCADE, related_name='Ordens')
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, related_name='Ordens')
    id_natureza_despesa = models.ForeignKey(NaturezasDespesa, on_delete=models.CASCADE, related_name='Ordens')
    numero = models.IntegerField()
    ano = models.IntegerField()
    
    class Meta:
        ordering = ["ano"]
        db_table = "Ordens"
        verbose_name_plural = "Ordens"

    #titulo_projeto - razao_social - numero
    def __str__(self) -> str:
        return self.id_projeto.titulo + ' - ' + self.id_fornecedor.razao_social + ' - ' + str(self.numero)    


class Contratos(DadosCadModel):
    id_contrato = models.AutoField(primary_key=True)
    id_prestador = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, related_name='Contratos')
    numero = models.IntegerField()
    ano = models.IntegerField()
    objeto = models.CharField(max_length=30)

    class Meta:
        ordering = ["ano"]
        db_table = "Contratos"
        verbose_name_plural = "Contratos"

    #IntelBras - 2021 - objeto
    def __str__(self) -> str:
        return self.id_prestador.razao_social +' - '+ str(self.ano) + ' - '+ self.objeto           




class Vigencias(models.Model):
    id_vigencia = models.AutoField(primary_key=True)
    id_contrato = models.OneToOneField(Contratos, on_delete=models.CASCADE)
    dt_inicio_vigencia = models.DateField()
    dt_fim_vigencia = models.DateField()

    class Meta:
        ordering = ['id_contrato']
        db_table = "Vigencias"
        verbose_name_plural = 'Vigencias'

        def __str__(self) -> str:
            return self.id_contrato







class ItensOrdem(DadosCadModel):
    id_item_ordem = models.AutoField(primary_key=True)
    id_ordem = models.ForeignKey(Ordens, on_delete=models.CASCADE)
    produto_servico = models.CharField(max_length=150)
    qtd = models.IntegerField()
    valor_unitario = models.FloatField()
    vinculado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['produto_servico']
        db_table = "ItensOrdem"
        verbose_name_plural = 'Itens Ordem'

    def __str__(self) -> str:
        return str(self.id_ordem) +' - '+ self.produto_servico
    



class ItensContratos(DadosCadModel):
    id_item_contrato = models.AutoField(primary_key=True)
    id_contrato = models.ForeignKey(Contratos, on_delete=models.CASCADE)
    id_item_ordem = models.ForeignKey(ItensOrdem, on_delete=models.CASCADE)
    qtd = models.IntegerField()
    valor_unitario = models.FloatField()
    
    class Meta:
        ordering = ['id_contrato']
        db_table = "ItensContratos"
        verbose_name_plural = 'Itens Contratos'

    def __str__(self) -> str:
        return self.id_contrato

