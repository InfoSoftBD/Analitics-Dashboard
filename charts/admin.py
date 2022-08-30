from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Performance)
admin.site.register(Deposit)
admin.site.register(Loan)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(KPI)