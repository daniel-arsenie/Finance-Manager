import django_filters
from django.forms import DateInput
from .models import Spending

# Used Flterset to filter the DB based on user choices from some Model fields on the page "All records"
class SpendingFilter(django_filters.FilterSet):
    date_time = django_filters.DateFilter(
        lookup_expr='gte', label='From',
        widget=DateInput(attrs={'type': 'date', 'id': 'start_date'}))

    class Meta:
        model = Spending
        fields = ['paid_with', 'record_type', 'date_time']
