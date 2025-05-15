from django import forms
from bankapp.models import Customer, Fellow, Type, Card

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class FellowCreationForm(forms.ModelForm):
    class Meta:
        model = Fellow
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'card': forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].queryset = Type.objects.none()

        if 'card' in self.data:
            try:
                card_id = int(self.data.get('card'))
                self.fields['type'].queryset = Type.objects.filter(card_id=card_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['type'].queryset = self.instance.card.type_set.order_by('name')

class DepositForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'})
    )

class WithdrawForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'})
    )

class CardSelectionForm(forms.Form):
    card = forms.ModelChoiceField(
        queryset=Card.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Select a card"
    )