from django.db import models

# Relatório meta vendedores
class VendasRelatorio(models.Model):
    id_venda = models.CharField(max_length=100, primary_key=True, db_column='ID_VENDA')
    codigo_vendedor = models.CharField(max_length=6, db_column='CODIGO_VENDEDOR')
    nome_vendedor = models.CharField(max_length=100, db_column='NOME_VENDEDOR')
    data_emissao = models.DateField(db_column='DATA_EMISSAO')
    codigo_produto = models.CharField(max_length=30, db_column='CODIGO_PRODUTO')
    descricao_produto = models.CharField(max_length=255, db_column='DESCRICAO_PRODUTO')

    class Meta:
        managed = False
        db_table = 'VW_VENDAS_RELATORIO'

# Relatório Duplicidade de NF venda assistida
class DuplicidadeNFRelatorio(models.Model):
    id_registro = models.CharField(max_length=50, primary_key=True, db_column='ID_REGISTRO')
    filial = models.CharField(max_length=10, db_column='FILIAL')
    numero_pedido = models.CharField(max_length=20, db_column='NUMERO_PEDIDO')
    cliente = models.CharField(max_length=20, db_column='CLIENTE')
    numero_nf = models.CharField(max_length=20, db_column='NUMERO_NF')
    serie_nf = models.CharField(max_length=10, db_column='SERIE_NF')
    mensagem_nota = models.CharField(max_length=255, db_column='MENSAGEM_NOTA')
    data_emissao = models.DateField(db_column='DATA_EMISSAO')

    class Meta:
        managed = False
        db_table = 'VW_DUPLICIDADE_NF'

# Relatório Contracheque APENAS PARA ADMIN
class ContrachequeRelatorio(models.Model):
   id_registro = models.CharField(max_length=100, primary_key=True, db_column='ID_REGISTRO')
   filial = models.CharField(max_length=10, db_column='FILIAL')
   matricula = models.CharField(max_length=20, db_column='MATRICULA')
   nome = models.CharField(max_length=100, db_column='NOME')
   descricao_verba = models.CharField(max_length=100, db_column='DESCRICAO_VERBA')
   tipo_verba = models.CharField(max_length=50, db_column='TIPO_VERBA')
   valor = models.DecimalField(max_digits=15, decimal_places=2, db_column='VALOR')
   data_pag = models.DateField(db_column='DATA_PAG')

   class Meta:
       managed = False
       db_table = 'VW_CONTRACHEQUE'