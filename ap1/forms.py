from django import forms
from ap1.models import Customer, Fellow, Type


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class FellowCreationForm(forms.ModelForm):
    class Meta:
        model = Fellow
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={ 'class': 'form-control' }),
                   'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
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
                pass  # invalid input from the client; ignore and fallback to empty type queryset
        elif self.instance.pk:
            self.fields['type'].queryset = self.instance.card.type_set.order_by('name')