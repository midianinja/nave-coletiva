from django.forms import ModelForm, Textarea
from festival.models import Atividade

class AtividadeAdminForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Atividade
        widgets = {
            'observacoes': Textarea(attrs={'rows': 2, 'cols': 80}),
        }
