"""
Created on Tue Jul  7 11:52:27 2020

@author: vanderneto
"""
from django import forms
import datetime



NuM=''

class palavraChave(forms.Form):
    palavra_chave1 = forms.CharField(required=False, max_length=100, label='Palavras-Chave')
    palavra_chave2 = forms.CharField(required=False, max_length=100)
    palavra_chave3 = forms.CharField(required=False, max_length=100)
   
class ProcessoNum():
    
    numero=''
    def __init__(self):
         print(self.numero)
    
    def recebe(self,data):
        self.numero = data
        NuM = data
        print(self.numero)
        
    def envia(self):
        print(self.numero)
        return self.numero
        

class ContactForm(forms.Form):
    
    print("Fomulario")
    print(NuM)
    areadocnpq = forms.CharField(max_length=100, label='Area do Conhecimento CNPq',)
    areaint = forms.CharField(max_length=100, label='Area do Conhecimento Internacional')
    op_assunto = [(num, name) for num, name in enumerate(open("./formuv1/listasubject.dat",'r'), start=1)]
    subject = forms.ChoiceField(choices=op_assunto, label='Assunto',)
    chamada = forms.CharField(max_length=100, label='Chamada',)
    conjdedados = forms.CharField(max_length=100, label='Conjunto de dados(URL)', help_text='Caso exista')
    title = forms.CharField(max_length=100, label='Dataset Title',)
    name = forms.CharField(max_length=100, label='Author Name',)
    affiliation = forms.CharField(max_length=100, label='Affiliation',)
    email = forms.EmailField(max_length=100, label='Author Email')    
    creater = forms.CharField(max_length=300, label='Coordenador do projeto')
    descrition_proj = forms.CharField(widget=forms.Textarea,label='Descrição do projeto')
    descrition_dataset = forms.CharField(widget=forms.Textarea,label='Descrição do dataset')
    descrition_proj = forms.CharField(widget=forms.Textarea,label='Descrição do projeto')
    financiador = forms.CharField(max_length=100, label='Financiador')
    id_alternativo = forms.CharField(required=False, max_length=100, label='ID do Autor(Handle)')
    inst_autor = forms.CharField(required=False, max_length=100, label='Instituição do Autor')
    num_proj = forms.CharField(required=False, max_length=100, label='Número do Projeto', initial="AAA")
    ori_coleta = forms.CharField(required=False, max_length=100, label='Origem da Coleta')
    financiadores = forms.CharField(required=False, max_length=100, label='Outros Financiadores')
    membros_proj = forms.CharField(required=False, max_length=100, label='Outros membros do projeto')
    op_tipos = [(num, name) for num, name in enumerate(open("./formuv1/listatipo.dat",'r'), start=1)]
    tiposdearquivo = forms.ChoiceField(choices=op_tipos, label='Tipos de arquivos')
    valorfinan=forms.CharField(required=False, max_length=100, label='Valor do Financiamento')
    versao = forms.CharField()
    data_dep = forms.DateField(initial=datetime.date.today, label='Data de depósito')
    data_vig = forms.DateField(label = 'Data de vigencia')
    #palavra_chave = palavraChave()
    
    docfile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Select a file', help_text='max. 42 megabytes')
    #docfile = forms.FileField(label='Select a file', help_text='max. 42 megabytes')
    #file = Upload
    
    
class ProcessoForm(forms.Form):
    processo = forms.CharField(required=False,max_length=300, label='Número do Processo', initial="dddddd/aaaa-v")
    token = forms.CharField(required=False,max_length=300, label='Token de autenticação')
    



         
         
        
        
        
        
    
