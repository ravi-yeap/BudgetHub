from django.contrib import admin
from .models import StudentProfile
from expenses.models import Expense


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'monthly_budget', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount', 'category', 'date', 'created_at')
    list_filter = ('category', 'date', 'created_at')
    search_fields = ('title', 'user__username', 'notes')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('user', 'title', 'amount', 'category')}),
        ('Details', {'fields': ('date', 'notes')}),
        ('Metadata', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )
