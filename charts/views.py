from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.core.exceptions import PermissionDenied # new
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from . forms import *
from .models import *
import pandas as pd

class kpiDetail(LoginRequiredMixin, DetailView): # new
	model = KPI
	template_name = 'forms/kpi_detail.html'
	login_url = 'login' # new

class kpiEdit(LoginRequiredMixin, UpdateView): # new
	model = KPI
	fields = ('description', 'amount',)
	template_name = 'forms/kpiedit.html'
	login_url = 'login' # new
	
	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class kpiDelete(LoginRequiredMixin, DeleteView): # new
	model = KPI
	template_name = 'forms/kpidelete.html'
	success_url = reverse_lazy('kpi')
	login_url = 'login' # new
	
	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class depositDetail(LoginRequiredMixin, DetailView): # new
	model = Deposit
	template_name = 'forms/deposit_detail.html'
	login_url = 'login' # new

class depositEdit(LoginRequiredMixin, UpdateView): # new
	model = Deposit
	fields = ('description', 'amount',)
	template_name = 'forms/depositedit.html'
	login_url = 'login' # new
	
	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

class depositDelete(LoginRequiredMixin, DeleteView): # new
	model = Deposit
	template_name = 'forms/depositdelete.html'
	success_url = reverse_lazy('deposit')
	login_url = 'login' # new
	
	def dispatch(self, request, *args, **kwargs): # new
		obj = self.get_object()
		if obj.author != self.request.user:
			raise PermissionDenied
		return super().dispatch(request, *args, **kwargs)

def home(request):
	deposits = Deposit.objects.all().values()
	loans = Loan.objects.all().values()
	incomes = Income.objects.all().values()
	expenses = Expense.objects.all().values()
	performances = Performance.objects.all().values()
	kpi = KPI.objects.all().values()
    
	dataPerformance=pd.DataFrame(performances)
	dataDeposit=pd.DataFrame(deposits)
	dataLoan=pd.DataFrame(loans)
	dataIncome=pd.DataFrame(incomes)
	dataExpense=pd.DataFrame(expenses)
	dataKpi=pd.DataFrame(kpi)
	
	labelPerformance=dataPerformance.description.tolist()
	figurePerformance=dataPerformance['amount'].tolist()
	labelDeposit=dataDeposit.description.tolist()
	figureDeposit=dataDeposit['amount'].tolist()
	labelLoan=dataLoan.description.tolist()
	figureLoan=dataLoan['amount'].tolist()
	labelIncome=dataIncome.description.tolist()
	figureIncome=dataIncome['amount'].tolist()
	labelExpense=dataExpense.description.tolist()
	figureExpense=dataExpense['amount'].tolist()
	labelKpi=dataKpi.description.tolist()
	figureKpi=dataKpi['amount'].tolist()
	
	mydict = {
		'labelPerformance':labelPerformance,
		'figurePerformance':figurePerformance,
		'labelDeposit':labelDeposit,
		'figureDeposit':figureDeposit,
		'labelLoan':labelLoan,
		'figureLoan':figureLoan,
		'labelIncome':labelIncome,
		'figureIncome':figureIncome,
		'labelExpense':labelExpense,
		'figureExpense':figureExpense,
		'labelKpi':labelKpi,
		'figureKpi':figureKpi
	}
	return render(request, 'index.html', context=mydict)

def positionView(request):
	deposits = Deposit.objects.all().values()
	loans = Loan.objects.all().values()
	incomes = Income.objects.all().values()
	expenses = Expense.objects.all().values()
	performances = Performance.objects.all().values()
	kpi = KPI.objects.all().values()
    
	dataPerformance=pd.DataFrame(performances)
	dataDeposit=pd.DataFrame(deposits)
	dataLoan=pd.DataFrame(loans)
	dataIncome=pd.DataFrame(incomes)
	dataExpense=pd.DataFrame(expenses)
	dataKpi=pd.DataFrame(kpi)
	
	labelPerformance=dataPerformance.description.tolist()
	figurePerformance=dataPerformance['amount'].tolist()
	labelDeposit=dataDeposit.description.tolist()
	figureDeposit=dataDeposit['amount'].tolist()
	labelLoan=dataLoan.description.tolist()
	figureLoan=dataLoan['amount'].tolist()
	labelIncome=dataIncome.description.tolist()
	figureIncome=dataIncome['amount'].tolist()
	labelExpense=dataExpense.description.tolist()
	figureExpense=dataExpense['amount'].tolist()
	labelKpi=dataKpi.description.tolist()
	figureKpi=dataKpi['amount'].tolist()
	
	mydict = {
		'labelPerformance':labelPerformance,
		'figurePerformance':figurePerformance,
		'labelDeposit':labelDeposit,
		'figureDeposit':figureDeposit,
		'labelLoan':labelLoan,
		'figureLoan':figureLoan,
		'labelIncome':labelIncome,
		'figureIncome':figureIncome,
		'labelExpense':labelExpense,
		'figureExpense':figureExpense,
		'labelKpi':labelKpi,
		'figureKpi':figureKpi
	}
	return render(request, 'home.html', context=mydict)

def index(request):
	deposits = Deposit.objects.all().values()
	loans = Loan.objects.all().values()
	incomes = Income.objects.all().values()
	expenses = Expense.objects.all().values()
	performances = Performance.objects.all().values()
    
	dataPerformance=pd.DataFrame(performances)
	dataDeposit=pd.DataFrame(deposits)
	dataLoan=pd.DataFrame(loans)
	dataIncome=pd.DataFrame(incomes)
	dataExpense=pd.DataFrame(expenses)
	
	labelPerformance=dataPerformance.description.tolist()
	figurePerformance=dataPerformance['amount'].tolist()
	labelDeposit=dataDeposit.description.tolist()
	figureDeposit=dataDeposit['amount'].tolist()
	labelLoan=dataLoan.description.tolist()
	figureLoan=dataLoan['amount'].tolist()
	labelIncome=dataIncome.description.tolist()
	figureIncome=dataIncome['amount'].tolist()
	labelExpense=dataExpense.description.tolist()
	figureExpense=dataExpense['amount'].tolist()
	
	mydict = {
		'labelPerformance':labelPerformance,
		'figurePerformance':figurePerformance,
		'labelDeposit':labelDeposit,
		'figureDeposit':figureDeposit,
		'labelLoan':labelLoan,
		'figureLoan':figureLoan,
		'labelIncome':labelIncome,
		'figureIncome':figureIncome,
		'labelExpense':labelExpense,
		'figureExpense':figureExpense
	}
	return render(request, 'forms/index.html', context=mydict)

def kpiEntry(request):
    kpis = KPI.objects.all()

    if request.method == 'POST':
        form = KpiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kpi')
    else:
        form = KpiForm()        

    context = {
        "kpis": kpis,
        "form": form
    }

    return render(request, 'forms/kpientry.html', context)


def depositEntry(request):
    deposits = Deposit.objects.all()

    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deposit')
    else:
        form = DepositForm()        

    context = {
        "deposits": deposits,
        "form": form
    }

    return render(request, 'forms/depositentry.html', context)




def loanEntry(request):
    loans = Loan.objects.all()

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan')
    else:
        form = LoanForm()        

    context = {
        "loans": loans,
        "form": form
    }

    return render(request, 'forms/loanentry.html', context)

def incomeEntry(request):
    incomes = Income.objects.all()

    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income')
    else:
        form = IncomeForm()        

    context = {
        "incomes": incomes,
        "form": form
    }

    return render(request, 'forms/incomeentry.html', context)

def expenseEntry(request):
    expenses = Expense.objects.all()

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense')
    else:
        form = ExpenseForm()        

    context = {
        "expenses": expenses,
        "form": form
    }

    return render(request, 'forms/expenseentry.html', context)

def performanceEntry(request):
    performances = Performance.objects.all()

    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance')
    else:
        form = PerformanceForm()        

    context = {
        "performances": performances,
        "form": form
    }

    return render(request, 'forms/performanceentry.html', context)
	
def position(request):
	item = Performance.objects.all().values()
	df=pd.DataFrame(item)
	df1=df.description.tolist()
	df=df['amount'].tolist()
	mydict = {
		'df':df,
		'df1':df1
	}
	return render(request, 'position.html', context=mydict)

	
def deposit(request):
	item = Deposit.objects.all().values()
	df=pd.DataFrame(item)
	df1=df.description.tolist()
	df=df['amount'].tolist()
	mydict = {
		'df':df,
		'df1':df1
	}
	return render(request, 'deposit.html', context=mydict)
	
def loan(request):
	item = Loan.objects.all().values()
	df=pd.DataFrame(item)
	df1=df.description.tolist()
	df=df['amount'].tolist()
	mydict = {
		'df':df,
		'df1':df1
	}
	return render(request, 'loan.html', context=mydict)
	
def income(request):
	item = Income.objects.all().values()
	df=pd.DataFrame(item)
	df1=df.description.tolist()
	df=df['amount'].tolist()
	mydict = {
		'df':df,
		'df1':df1
	}
	return render(request, 'income.html', context=mydict)
	
def expense(request):
	item = Expense.objects.all().values()
	df=pd.DataFrame(item)
	df1=df.description.tolist()
	df=df['amount'].tolist()
	mydict = {
		'df':df,
		'df1':df1
	}
	return render(request, 'expense.html', context=mydict)