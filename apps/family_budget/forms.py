from django.forms import ModelForm, TextInput, Textarea

from core import settings
from .models import Budget


class BudgetForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = settings.DATE_INPUT_FORMATS

    class Meta:
        model = Budget
        fields = ['date', 'amount_spent', 'description']

        widgets = {
            'date': TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'format dd.mm.YYYY',
            }),
            'amount_spent': TextInput(attrs={
                'class': 'form-input',
            }),
            'description': Textarea(attrs={
                'cols': 60,
                'rows': 10,
            }),
        }
