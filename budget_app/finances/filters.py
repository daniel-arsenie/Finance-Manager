import django_filters
from django.forms import DateInput
from django_filters import DateFromToRangeFilter, OrderingFilter

from . import forms
from .models import Spending


class SpendingFilter(django_filters.FilterSet):
    date_time = django_filters.DateFilter(
        lookup_expr='gte', label='From',
        widget=DateInput(attrs={'type': 'date', 'id': 'start_date'}))

    o = OrderingFilter(
        fields=(
            ('date_time', 'date_time'),
        )
    )

    class Meta:
        model = Spending
        fields = ['paid_with', 'record_type', 'date_time']
