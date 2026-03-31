from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list_view, name='expense_list'),
    path('add/', views.add_expense_view, name='add_expense'),
    path('<int:pk>/edit/', views.edit_expense_view, name='edit_expense'),
    path('<int:pk>/delete/', views.delete_expense_view, name='delete_expense'),
    path('recent/', views.recent_expenses_view, name='recent_expenses'),
]
