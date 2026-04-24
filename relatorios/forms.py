from django import forms 
from django.contrib.auth.models import Group

# Cadastro de Usuários
class CadastroUsuarioForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário (Login)', max_length=150)
    email = forms.EmailField(label='E-mail', required=False)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    # O ModelChoiceField cria um select automático puxando os grupos do banco
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=False,
        empty_label="Sem módulo (Apenas Login)",
        label='Módulo de Acesso'
    )

# Cadastro de Módulos de acesso
class CadastroModuloForm(forms.Form):
    nome = forms.CharField(label='Nome do Módulo', max_length=100)

# Relatório meta vendedores
class FiltroRelatorioForm(forms.Form):
    vendedor = forms.CharField(required=False, label='Vendedor (Código)')
    data_de = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Emissao De')
    data_ate = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Emissao ate')
    produto = forms.CharField(required=False, label='Descrição do Produto')

# Relatório Duplicidade de NF venda assistida
class FiltroDuplicidadeNFForm(forms.Form):
    filial = forms.CharField(required=False, label='Filial')
    mensagem = forms.CharField(required=False, label='Mensagem da NF')
    data_de = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Emissão De')
    data_ate = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Emissão ate')

# Relatório Contracheque
class FiltroContrachequeForm(forms.Form):
    filial = forms.CharField(required=False, label='Filial')
    matricula = forms.CharField(required=False, label='Matricula')
    data_de = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Data De')
    data_ate = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Data ate')
