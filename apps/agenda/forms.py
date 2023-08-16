from django import forms

from apps.agenda.models import Fotografia
from apps.agenda.models import FazerMeta
from apps.agenda.models import FazerAnotacao

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada',]
        labels ={
            'descricao':'Descrição',
            'data_evento': 'Data de registro',
            'usuario': 'Usuário',
        }
        
        
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'legenda': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'data_evento': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),  # Adicione esta linha
        }
        
        
        
        
class FotografiaForm(forms.ModelForm):
    # Defina as opções para o campo "estado"
    OPCOES_ESTADO = [
        ('Em andamento', 'Em andamento'),
        ('Concluido', 'Concluido'),
    ]

    # Adicione o campo "estado" ao formulário com as opções definidas
    estado = forms.ChoiceField(choices=OPCOES_ESTADO, initial='Em andamento',)

    class Meta:
        model = Fotografia
        fields = ['nome', 'legenda', 'categoria', 'descricao', 'foto', 'data_evento', 'usuario', 'estado']
        
        
     
class FazerMetaForm(forms.ModelForm):
    class Meta:
        model = FazerMeta
        fields = ['nomeMeta', 'data_inicio', 'data_fim', 'quantidade_passos', 'modo']
        widgets = {
            'nomeMeta': forms.TextInput(attrs={'class': 'form-control'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control date-picker', 'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control date-picker', 'type': 'date'}),
            'quantidade_passos': forms.NumberInput(attrs={'class': 'form-control'}),
            'modo': forms.Select(attrs={'class': 'form-control'}),
        }
        
from django import forms
from .models import FazerAnotacao

class FazerAnotacaoForm(forms.ModelForm):
    class Meta:
        model = FazerAnotacao
        fields = ['nomeAnotacao', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'nomeAnotacao': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
