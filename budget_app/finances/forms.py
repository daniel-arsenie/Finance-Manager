from django import forms
from django.forms import ModelForm
from .models import Spending


# Create a spending form
# Used ModelForm because it has built-in functions to help in using forms (it does the GET and POST by itself)
class SpendingForm(ModelForm):
    class Meta:
        model = Spending
        fields = ('record_type', 'paid_with', 'amount', 'category', 'date_time', 'location', 'description')
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
