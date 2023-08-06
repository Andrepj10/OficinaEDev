from django import forms

from apps.agenda.models import Fotografia
from apps.agenda.models import FazerMeta

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
        
        