import django
from django.conf import settings
from django.urls import path
from django.views.generic import RedirectView

django.setup()

urlpatterns = [
    path('', RedirectView.as_view(url='analytics/dashboard/', permanent=False), name='index'),
]
