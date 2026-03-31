from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Expense
from .forms import ExpenseForm, ExpenseFilterForm


@login_required(login_url='login')
def expense_list_view(request):
    """View all expenses with filtering and search."""
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    form = ExpenseFilterForm(request.GET)
    
    # Apply filters
    if form.is_valid():
        category = form.cleaned_data.get('category')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        search = form.cleaned_data.get('search')
        
        if category:
            expenses = expenses.filter(category=category)
        
        if start_date:
            expenses = expenses.filter(date__gte=start_date)
        
        if end_date:
            expenses = expenses.filter(date__lte=end_date)
        
        if search:
            expenses = expenses.filter(
                Q(title__icontains=search) |
                Q(notes__icontains=search)
            )
    
    # Pagination context
    total_expenses = expenses.count()
    total_spent = sum(exp.amount for exp in expenses)
    
    context = {
        'expenses': expenses[:50],  # Limit to 50 for display
        'form': form,
        'total_expenses': total_expenses,
        'total_spent': total_spent,
    }
    
    return render(request, 'expenses/expense_list.html', context)


@login_required(login_url='login')
def add_expense_view(request):
    """Add a new expense."""
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    
    return render(request, 'expenses/add_expense.html', {'form': form})


@login_required(login_url='login')
def edit_expense_view(request, pk):
    """Edit an existing expense."""
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'expenses/edit_expense.html', {'form': form, 'expense': expense})


@login_required(login_url='login')
def delete_expense_view(request, pk):
    """Delete an expense."""
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    
    if request.method == 'POST':
        title = expense.title
        expense.delete()
        messages.success(request, f'Expense "{title}" deleted successfully!')
        return redirect('expense_list')
    
    return render(request, 'expenses/delete_expense.html', {'expense': expense})


@login_required(login_url='login')
def recent_expenses_view(request):
    """Get recent expenses for API/AJAX."""
    expenses = Expense.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'expenses/recent_expenses.html', {'expenses': expenses})
