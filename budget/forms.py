from django import forms


class BudgetForm(forms.Form):
    """Form for setting monthly budget."""
    monthly_budget = forms.DecimalField(
        label='Monthly Budget',
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        widget=forms.NumberInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': '0.00',
            'step': '0.01',
            'min': '0.01'
        }),
        help_text='Enter your monthly budget limit'
    )
