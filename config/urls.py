"""
URL Configuration for Student Budget Manager project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='analytics/dashboard/', permanent=False), name='index'),
    path('', include('accounts.urls')),
    path('expenses/', include('expenses.urls')),
    path('budget/', include('budget.urls')),
    path('analytics/', include('analytics.urls')),
]
