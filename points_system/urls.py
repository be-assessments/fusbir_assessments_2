"""
URL configuration for points_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from transactions import views

urlpatterns = [
    path('get_all', views.GetAllTransactionsView.as_view(), name='get_all_transactions'),
    path('add_transaction', views.AddTransactionView.as_view(), name='add_transaction'),
    path('add_bulk_transactions/', views.AddBulkTransactionsView.as_view(), name='add_bulk_transactions'),
    path('spend/', views.SpendPointsView.as_view(), name='spend_points'),
    path('balance/', views.GetBalanceView.as_view(), name='get_balance'), 
]


