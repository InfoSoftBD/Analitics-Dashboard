from django.urls import path
from .import views
from .views import *
from .views import (
	depositEdit,
	depositDelete,
	depositDetail,
	kpiEdit,
	kpiDelete,
	kpiDetail,
	positionView,
)

urlpatterns = [
	path('index/', views.index,name='index'),
	path('performance/', views.performanceEntry,name='performance'),
	path('deposit/', views.depositEntry,name='deposit'),
	path('kpi/', views.kpiEntry,name='kpi'),
	path('loan/', views.loanEntry,name='loan'),
	path('income/', views.incomeEntry,name='income'),
	path('expense/', views.expenseEntry,name='expense'),
	path('position/', views.positionView,name='positionView'),
	
	
	path('<int:pk>/depositedit/', depositEdit.as_view(), name='depositedit'), # new
	path('<int:pk>/depositdetail/', depositDetail.as_view(), name='deposit_detail'), # new
	path('<int:pk>/ddepositdelete/', depositDelete.as_view(), name='depositdelete'), # new
	
	path('<int:pk>/kpiedit/', kpiEdit.as_view(), name='kpiedit'), # new
	path('<int:pk>/kpidetail', kpiDetail.as_view(), name='kpi_detail'), # new
	path('<int:pk>/kpidelete/', kpiDelete.as_view(), name='kpidelete'), # new
		
    path('', views.home,name='home')
]
