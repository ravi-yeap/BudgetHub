from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from accounts.models import StudentProfile
from expenses.models import Expense
from .forms import BudgetForm


@login_required(login_url='login')
def budget_view(request):
    """View and set monthly budget."""
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            student_profile.monthly_budget = form.cleaned_data['monthly_budget']
            student_profile.save()
            messages.success(request, 'Monthly budget updated successfully!')
            return redirect('budget')
    else:
        form = BudgetForm(initial={'monthly_budget': student_profile.monthly_budget})
    
    # Calculate total expenses
    total_expenses = request.user.expenses.aggregate(total=Sum('amount'))['total'] or 0
    expense_count = request.user.expenses.count()
    
    # Calculate budget percentage
    if student_profile.monthly_budget > 0:
        budget_percentage = (total_expenses / student_profile.monthly_budget) * 100
        if budget_percentage >= 100:
            budget_status = 'Exceeded'
            status_color = 'red'
        elif budget_percentage >= 80:
            budget_status = 'Warning'
            status_color = 'yellow'
        else:
            budget_status = 'On Track'
            status_color = 'green'
    else:
        budget_percentage = 0
        budget_status = 'Set a budget'
        status_color = 'gray'
    
    remaining_budget = student_profile.monthly_budget - total_expenses
    
    context = {
        'form': form,
        'student_profile': student_profile,
        'total_expenses': total_expenses,
        'expense_count': expense_count,
        'budget_percentage': budget_percentage,
        'budget_status': budget_status,
        'status_color': status_color,
        'remaining_budget': remaining_budget,
    }
    
    return render(request, 'budget/budget.html', context)
