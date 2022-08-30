from django import forms
from . models import *

class KpiForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = '__all__'
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
        }
