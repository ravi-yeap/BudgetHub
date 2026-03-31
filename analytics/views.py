from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime, timedelta
from decimal import Decimal
from accounts.models import StudentProfile
from expenses.models import Expense
import json


@login_required(login_url='login')
def dashboard_view(request):
    """Main dashboard view with analytics."""
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    
    # Get all expenses for the user
    expenses = Expense.objects.filter(user=request.user)
    
    # Total spent
    total_spent = expenses.aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
    
    # Remaining balance
    remaining_balance = student_profile.monthly_budget - total_spent
    
    # Budget percentage used
    if student_profile.monthly_budget > 0:
        budget_percentage = (total_spent / student_profile.monthly_budget) * 100
    else:
        budget_percentage = 0
    
    # Recent expenses
    recent_expenses = expenses.order_by('-date')[:5]
    
    # Weekly breakdown
    weekly_data = get_weekly_spending_data(request.user)
    
    # Category breakdown
    category_data = get_category_breakdown_data(request.user)
    
    # Budget status
    if budget_percentage >= 100:
        budget_status = 'exceeded'
    elif budget_percentage >= 80:
        budget_status = 'warning'
    else:
        budget_status = 'safe'
    
    context = {
        'student_profile': student_profile,
        'total_spent': total_spent,
        'remaining_balance': remaining_balance,
        'budget_percentage': min(budget_percentage, 100),
        'recent_expenses': recent_expenses,
        'weekly_data': json.dumps(weekly_data),
        'category_data': json.dumps(category_data),
        'budget_status': budget_status,
        'total_expenses_count': expenses.count(),
    }
    
    return render(request, 'dashboard/dashboard.html', context)


def get_weekly_spending_data(user):
    """Get spending data for the last 7 days."""
    today = timezone.now().date()
    dates = [(today - timedelta(days=i)).strftime('%a') for i in range(6, -1, -1)]
    
    weekly_data = {
        'labels': dates,
        'data': []
    }
    
    for i in range(6, -1, -1):
        date = today - timedelta(days=i)
        daily_spent = Expense.objects.filter(
            user=user,
            date=date
        ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        weekly_data['data'].append(float(daily_spent))
    
    return weekly_data


def get_category_breakdown_data(user):
    """Get category breakdown data."""
    categories = Expense.objects.filter(user=user).values('category').annotate(
        total=Sum('amount')
    ).order_by('-total')
    
    category_map = {choice[0]: choice[1] for choice in Expense.CATEGORY_CHOICES}
    
    return {
        'labels': [category_map.get(cat['category'], cat['category']) for cat in categories],
        'data': [float(cat['total']) for cat in categories],
        'backgroundColor': [
            '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0',
            '#9966FF', '#FF9F40', '#FF6384'
        ][:len(categories)]
    }


@login_required(login_url='login')
def analytics_view(request):
    """Detailed analytics page."""
    student_profile = get_object_or_404(StudentProfile, user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    
    # Monthly summary
    today = timezone.now().date()
    month_start = today.replace(day=1)
    month_expenses = expenses.filter(date__gte=month_start)
    
    total_spent_month = month_expenses.aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
    total_expenses_count = expenses.count()
    
    # Calculate average expense
    if total_expenses_count > 0:
        average_expense = total_spent_month / total_expenses_count
    else:
        average_expense = Decimal('0.00')
    
    # Category breakdown with counts
    category_stats = month_expenses.values('category').annotate(
        total=Sum('amount'),
        count=Count('id')
    ).order_by('-total')
    
    category_map = {choice[0]: choice[1] for choice in Expense.CATEGORY_CHOICES}
    category_stats = [
        {
            'name': category_map.get(stat['category'], stat['category']),
            'total': stat['total'],
            'count': stat['count'],
            'percentage': float((stat['total'] / total_spent_month * 100)) if total_spent_month > 0 else 0
        }
        for stat in category_stats
    ]
    
    # Monthly trend (last 6 months)
    monthly_trend = get_monthly_trend_data(request.user)
    
    context = {
        'student_profile': student_profile,
        'total_spent_month': total_spent_month,
        'category_stats': category_stats,
        'monthly_trend': json.dumps(monthly_trend),
        'total_expenses': total_expenses_count,
        'average_expense': average_expense,
    }
    
    return render(request, 'dashboard/analytics.html', context)


def get_monthly_trend_data(user):
    """Get monthly spending trend for last 6 months."""
    today = timezone.now().date()
    months = []
    data = []
    
    for i in range(5, -1, -1):
        month_date = today - timedelta(days=30*i)
        month_start = month_date.replace(day=1)
        
        # Get next month's first day
        if month_date.month == 12:
            month_end = month_date.replace(year=month_date.year + 1, month=1, day=1)
        else:
            month_end = month_date.replace(month=month_date.month + 1, day=1)
        
        month_label = month_date.strftime('%b %Y')
        months.append(month_label)
        
        monthly_spent = Expense.objects.filter(
            user=user,
            date__gte=month_start,
            date__lt=month_end
        ).aggregate(Sum('amount'))['amount__sum'] or Decimal('0.00')
        
        data.append(float(monthly_spent))
    
    return {
        'labels': months,
        'data': data
    }
